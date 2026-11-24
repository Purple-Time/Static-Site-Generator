import os
import shutil
from recursive_copier import recursive_copier
from genpages_recursive import generate_pages_recursive


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    recursive_copier("static", "public")

    generate_pages_recursive("content", "template.html", "public")

main()
