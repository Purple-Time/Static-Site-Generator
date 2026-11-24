import os
import sys
import shutil
from recursive_copier import recursive_copier
from genpages_recursive import generate_pages_recursive


def main():

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists("docs"):
        shutil.rmtree("docs")
    os.mkdir("docs")
    recursive_copier("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
