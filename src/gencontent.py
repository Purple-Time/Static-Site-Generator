from block_to_html import markdown_to_html_node
import os


def extract_title(markdown):
    split = markdown.split("\n")
    for s in split:
        if s.startswith("# "):
            almost = s[2:]
            result = almost.strip()
            return result
    raise Exception("No header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_temp = f.read()
    with open(template_path) as t:
        template_temp = t.read()
    from_html = markdown_to_html_node(from_temp).to_html()
    title = extract_title(from_temp)
    template_temp = template_temp.replace("{{ Title }}", title)
    template_temp = template_temp.replace("{{ Content }}", from_html)
    folder = os.path.dirname(dest_path)
    os.makedirs(folder, exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(template_temp)
