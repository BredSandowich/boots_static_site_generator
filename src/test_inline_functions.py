import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link


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
            
    #Test extracting markdown from images and links
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an image ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
        "This is text with an link [anchor](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("anchor", "https://www.youtube.com/@bootdotdev")], matches)


    #Test link and image node splitting functionality
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with an [alt](www.boot.dev) and another [alt 2](www.youtube.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("alt", TextType.LINK, "www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "alt 2", TextType.LINK, "www.youtube.com"
                ),
            ],
            new_nodes,
        )

    
if __name__ == "__main__":
    unittest.main()