import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks, markdown_to_html_node

class Test_markdown_blocks(unittest.TestCase):
    #Tests for markdown_to_blocks
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
        
    def test_markdown_to_blocks_newlines(self):
        md = """
    This is block 1


    This is block 2



    This is block 3
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is block 1",
                "This is block 2",
                "This is block 3",
            ],
        )
    
    def test_markdown_to_blocks_whitespace(self):
        md = "  This is a block with leading/trailing spaces   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["This is a block with leading/trailing spaces"]
        )
        
    def test_markdown_to_blocks_mixed(self):
        md = """
# Heading

- Item 1
- Item 2

Paragraph with
multiple lines.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading",
                "- Item 1\n- Item 2",
                "Paragraph with\nmultiple lines.",
            ],
        )
        
    def test_markdown_to_blocks_empty(self):
        md = "          "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
        
     


#Testing for block_to_block_type

    #test for too many hashtags for heading
    def test_almost_heading(self):
        block = "####### Too many hashes"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_almost_heading_2(self):
        block = "###NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    #Test for missing > in quotation
    def test_almost_quote(self):
        block = "> This is a quote\nThis line is missing the symbol"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    #Test for ordered list to start with number 1
    def test_broken_Olist(self):
        block = "2. Starting with two\n3. Next line"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    #Test for unordered list with no space after -
    def test_broken_Ulist(self):
        block = "-No space after dash"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    #Test for code block logic
    def test_multi_line_code(self):
        block = "```\nprint('hello')\nprint('world')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    #Test if markdown gets assembled properly  
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
    
    
if __name__ == "__main__":
    unittest.main()