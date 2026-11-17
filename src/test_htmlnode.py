import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_prop_is_none(self):
        node = HTMLNode()
        html_test = node.props_to_html()
        self.assertEqual(html_test, (""))

    def test_prop_is_empty(self):
        node = HTMLNode(props={})
        html_test = node.props_to_html()
        self.assertEqual(html_test, (""))

    def test_props_to_html_works(self):
        a = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=a)
        html_test = node.props_to_html()
        self.assertEqual(html_test, (' href="https://www.google.com" target="_blank"'))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children_empty(self):
        node = ParentNode("p", [])
        self.assertEqual(
           node.to_html(), "<p></p>"
        )


if __name__ == "__main__":
    unittest.main()
