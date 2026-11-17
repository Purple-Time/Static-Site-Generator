import re
from textnode import *



def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        split_message = node.text.split(delimiter)
        if len(split_message) % 2 == 0:
            raise Exception('Hanging delimiter!')
        counter = 0
        for message in split_message:
            if (counter % 2) == 0:
                if message == "":
                    counter += 1
                    continue
                final_list.append(TextNode(split_message[counter], TextType.TEXT))
                counter += 1
            else:
                if message == "":
                    counter += 1
                    continue
                final_list.append(TextNode(split_message[counter], text_type))
                counter += 1
    return final_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        a = extract_markdown_images(node.text)
        if not a:
            final_list.append(node)
        else:
            regex_new = re.findall(r"!\[[^\[\]]*\]\([^\(\)]*\)", node.text)
            if len(regex_new) == 1:
                text_finder = node.text.split(regex_new[0], 1)
                if text_finder[0] != "":
                    final_list.append(TextNode(text_finder[0], TextType.TEXT))
                image_extract = extract_markdown_images(node.text)
                final_list.append(TextNode(image_extract[0][0], TextType.IMAGE, image_extract[0][1]))
                if text_finder[1] != "":
                    final_list.append(TextNode(text_finder[1], TextType.TEXT))
            else:
                internal_list = []
                text_finder = node.text.split(regex_new[0], 1)
                if text_finder[0] != "":
                    internal_list.append(TextNode(text_finder[0], TextType.TEXT))
                image_extract = extract_markdown_images(node.text)
                internal_list.append(TextNode(image_extract[0][0], TextType.IMAGE, image_extract[0][1]))
                if text_finder[1] != "":
                    internal_list.append(TextNode(text_finder[1], TextType.TEXT))
                recursive_list = split_nodes_image(internal_list)
                for item in recursive_list:
                    final_list.append(item)
    return final_list

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    final_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_list.append(node)
            continue
        a = extract_markdown_links(node.text)
        if not a:
            final_list.append(node)
        else:
            regex_new = re.findall(r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))", node.text)
            if len(regex_new) == 1:
                text_1 = node.text
                match = re.search(r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))", text_1)
                before = text_1[:match.start()]
                after = text_1[match.end():]
                if before != "":
                    final_list.append(TextNode(before, TextType.TEXT))
                link_extract = extract_markdown_links(node.text)
                final_list.append(TextNode(link_extract[0][0], TextType.LINK, link_extract[0][1]))
                if after != "":
                    final_list.append(TextNode(after, TextType.TEXT))
            else:
                internal_list = []
                text_1 = node.text
                match = re.search(r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))", text_1)
                before = text_1[:match.start()]
                after = text_1[match.end():]
                if before != "":
                    internal_list.append(TextNode(before, TextType.TEXT))
                link_extract = extract_markdown_links(node.text)
                internal_list.append(TextNode(link_extract[0][0], TextType.LINK, link_extract[0][1]))
                if after != "":
                    internal_list.append(TextNode(after, TextType.TEXT))
                recursive_list = split_nodes_link(internal_list)
                for item in recursive_list:
                    final_list.append(item)
    return final_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    final = link
    return final
