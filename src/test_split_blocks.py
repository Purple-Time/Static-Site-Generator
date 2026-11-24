import unittest
from split_blocks import *


class TestSplitBlocks(unittest.TestCase):


    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_empty_block_stripping(self):
        md = """
First paragraph



Second paragraph after extra blank lines
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "First paragraph",
                    "Second paragraph after extra blank lines",
                ],
            )

    def test_quote_block(self):
        md = """
> This is a quote
> spanning two lines

A regular paragraph after it
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "> This is a quote\n> spanning two lines",
                    "A regular paragraph after it",
                ],
            )
