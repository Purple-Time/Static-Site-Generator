import unittest
from block_to_html import *


class TestTextNode(unittest.TestCase):
    def test_everything(self):
        md = """
#### Subheading title

This is **bolded** paragraph
text in a p
tag here

> This is a quote
> that spans two lines

- First item
- Second item with _italic_
- Third item with `code`

1. First step
2. Second step
3. Third step

```
some code with _underscores_
and **stars** that must stay as-is
```

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """<div><h4>Subheading title</h4><p>This is <b>bolded</b> paragraph text in a p tag here</p><blockquote>This is a quote that spans two lines</blockquote><ul><li>First item</li><li>Second item with <i>italic</i></li><li>Third item with <code>code</code></li></ul><ol><li>First step</li><li>Second step</li><li>Third step</li></ol><pre><code>some code with _underscores_
and **stars** that must stay as-is
</code></pre><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>""",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
