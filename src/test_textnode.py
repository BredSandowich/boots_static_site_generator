import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    #Test the TextNode's
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_difpareq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This has different text alone", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_difpareq2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This has different text alone", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_difparequrl(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    #Test the TextNode's text_node_to_html_node()
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_LINK(self):
        node = TextNode("This has been fun", TextType.LINK, "www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This has been fun")
        self.assertEqual(html_node.props, {"href":"www.boot.dev"})
        
    
    def test_IMG(self):
        node = TextNode("This is a cool image", TextType.IMAGE, "www.brearbearsbrears")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"www.brearbearsbrears", "alt":"This is a cool image"})
    


if __name__ == "__main__":
    unittest.main()