import unittest
from blocktype import *


class TestBlockType(unittest.TestCase):



    def test_heading_block(self):
        md = "### Subheading title"
        blocks = block_to_block_type(md)
        self.assertEqual(
                blocks, BlockType.HEADING)

    def test_code_block(self):
        code_block = """```
code goes here```"""
        blocks = block_to_block_type(code_block)
        self.assertEqual(
                blocks, BlockType.CODE)

    def test_quote_block(self):
        md = "> This is the first line of a quote.\n>This is the second line without a space."
        blocks = block_to_block_type(md)
        self.assertEqual(
                blocks, BlockType.QUOTE)

    def test_ulist_block(self):
        md = "- First item\n- Second item\n- Third item"
        blocks = block_to_block_type(md)
        self.assertEqual(
                blocks, BlockType.UNORDERED_LIST)

    def test_olist_block(self):
        md = "1. First item\n2. Second item\n3. Third item"
        blocks = block_to_block_type(md)
        self.assertEqual(
                blocks, BlockType.ORDERED_LIST)
