import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "id": "main"})
        self.assertEqual(
            node.props_to_html(), 
            ' class="greeting" id="main"',
        )
        
    def test_multi_property(self):
        node = HTMLNode("p", "Some inner font on a p", None, {"href": "https://www.google.com", "target": "_blank",})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
        
    def test_no_properties(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(
            node.props_to_html(), 
            "",
        )
        
    def test_different_attributes(self):
        node = HTMLNode("p", "Some inner font on a p", None, {"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected) 


if __name__ == "__main__":
    unittest.main()