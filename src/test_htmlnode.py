import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    #Test HTMLNodes
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

    #Test Leafnodes
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
        
    #Test Parentnodes
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
        
    def test_to_html_with_grandchildren_deep_nesting(self):
        great_grandchild_node = LeafNode("b", "greatgrandchild")
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><span><b>greatgrandchild</b></span></p></div>",
        )
    
    def test_to_html_parent_properties(self):
        child_node = LeafNode("p", "child_node")
        parent_node = ParentNode("div", [child_node], {"class": "poopy"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="poopy"><p>child_node</p></div>',
        )


if __name__ == "__main__":
    unittest.main()