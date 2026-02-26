import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class Testsplit_nodes_delimiter(unittest.TestCase):
    #Test if node has multiple instances of delimiter
    def test_multi_delim(self):
        node = split_nodes_delimiter([TextNode("This is *has* *two* sets of delimiters",TextType.TEXT)], "*", TextType.ITALIC)
        self.assertEqual(node, 
                         [
                            TextNode("This is ", TextType.TEXT),
                            TextNode("has", TextType.ITALIC),
                            TextNode(" ", TextType.TEXT),
                            TextNode("two", TextType.ITALIC),
                            TextNode(" sets of delimiters", TextType.TEXT),
                        ])
        
    #Test if delimiter at the very beginning of a node works properly
    def test_delim_at_start(self):
        node = split_nodes_delimiter([TextNode("**This** delimiter is at the very beginning", TextType.TEXT)], "**", TextType.BOLD)
        self.assertEqual(node, 
                         [
                            TextNode("This", TextType.BOLD),
                            TextNode(" delimiter is at the very beginning", TextType.TEXT),
                        ])
        
    #Test multi delimiter types in a node
    def test_mixed_delim(self):
        node = split_nodes_delimiter([TextNode("already bold", TextType.BOLD), TextNode("some *italic* text", TextType.TEXT)], "*", TextType.ITALIC)
        self.assertEqual(node, 
                         [
                            TextNode("already bold", TextType.BOLD),
                            TextNode("some ", TextType.TEXT),
                            TextNode("italic", TextType.ITALIC),
                            TextNode(" text", TextType.TEXT),
                        ])
        
    #Test error of only 1 delimiter
    def test_one_delim(self):
        node = TextNode("**This is an improper delimiter case",TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)