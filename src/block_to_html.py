from split_blocks import markdown_to_blocks
from blocktype import *
from htmlnode import *
from split_nodes import *


def children_maker(text):
    html_node = text_node_to_html_node(text)
    return html_node

def paragraph_maker(block):
    split = block.split("\n")
    new_block = " ".join(split)
    text_nodes = text_to_textnodes(new_block)
    children = []
    for text in text_nodes:
        children.append(children_maker(text))
    return ParentNode("p", children)

def header_helper(block):
    if block[0] == "#":
        if block[1] == "#":
            if block[2] == "#":
                if block[3] == "#":
                    if block[4] == "#":
                        if block[5] == "#":
                            return ("h6", block[7:])
                        return ("h5", block[6:])
                    return ("h4", block[5:])
                return ("h3", block[4:])
            return ("h2", block[3:])
        return ("h1", block[2:])
    else:
        return ("???", "???")

def heading_maker(block):

    h_value, new_block = header_helper(block)

    text_nodes = text_to_textnodes(new_block)
    children = []
    for text in text_nodes:
        children.append(children_maker(text))
    return ParentNode(h_value, children)

def quote_maker(block):
    split = block.split("\n")
    split_1 = list(map(lambda p: p[1:], split))
    split_2 = list(map(lambda q: q.lstrip(), split_1))
    new_block = (" ").join(split_2)
    text_nodes = text_to_textnodes(new_block)
    children = []
    for text in text_nodes:
        children.append(children_maker(text))
    return ParentNode("blockquote", children)

def unordered_list_maker(block):
    split = block.split("\n")
    split_1 = list(map(lambda p: p[1:], split))
    baby_blocks = list(map(lambda q: q.lstrip(), split_1))
    baby_parents = []
    for block in baby_blocks:
        text_nodes = text_to_textnodes(block)
        children = []
        for text in text_nodes:
            children.append(children_maker(text))
        baby_parent = ParentNode("li", children)
        baby_parents.append(baby_parent)
    return ParentNode("ul", baby_parents)

def ordered_list_maker(block):
    split = block.split("\n")
    split_1 = list(map(lambda p: p[2:], split))
    baby_blocks = list(map(lambda q: q.lstrip(), split_1))
    baby_parents = []
    for block in baby_blocks:
        text_nodes = text_to_textnodes(block)
        children = []
        for text in text_nodes:
            children.append(children_maker(text))
        baby_parent = ParentNode("li", children)
        baby_parents.append(baby_parent)
    return ParentNode("ol", baby_parents)

def code_maker(block):

    split = block.split("\n")

    new_split = split[1:]

    joined = "\n".join(new_split)

    final = joined[:-3]

    text_node = TextNode(final, TextType.TEXT)
    html = text_node_to_html_node(text_node)
    code = ParentNode("code", [html])
    return ParentNode("pre", [code])

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    super_children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            result = paragraph_maker(block)

        elif block_type == BlockType.HEADING:
            result = heading_maker(block)

        elif block_type == BlockType.QUOTE:
            result = quote_maker(block)

        elif block_type == BlockType.UNORDERED_LIST:
            result = unordered_list_maker(block)

        elif block_type == BlockType.ORDERED_LIST:
            result = ordered_list_maker(block)

        elif block_type == BlockType.CODE:
            result = code_maker(block)


        super_children.append(result)

    return ParentNode("div", super_children)
