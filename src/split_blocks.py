



def markdown_to_blocks(markdown):
    final_list = []
    split_text = markdown.split("\n\n")
    stripped_split = []
    for text in split_text:
        a = text.strip()
        stripped_split.append(a)
    final_list = []
    for item in stripped_split:
        new_split = item.split("\n")
        if new_split == [""]:
            continue
        final_list.append(item)
    return final_list
