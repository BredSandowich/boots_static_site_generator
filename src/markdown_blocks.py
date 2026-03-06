from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes, text_node_to_html_node
from textnode import TextNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

#Take raw markdown string and return a list of "block" strings
def markdown_to_blocks(text):
    blocked = text.split("\n\n")
    new_list = []
    for block in blocked:
        trimmed = block.strip()
        if trimmed != "":
            new_list.append(trimmed)
    return new_list


#Takes a single block of markdown text as input and returns BlockType enum representing the type of block it is
def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith(f"1. "):
        order = 1
        for line in lines:
            if not line.startswith(f"{order}. "):
                return BlockType.PARAGRAPH
            order += 1
        return BlockType.ORDERED_LIST
        
    
    return BlockType.PARAGRAPH

#Helper functions to get HTML Tags from Markdown Block
def block_to_heading(block):
    split = block.split(" ", 1)
    header_num = split[0].count("#")
    
    content = split[1].strip()
    
    children = text_to_children(content)
    return ParentNode(f"h{header_num}", children)
        
    
def block_to_quote(block):
    lines = block.split("\n")
    quote = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        quote.append(line.lstrip(">").strip)
    content = " ".join(quote)
    
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def block_to_uolist(block):
    lines = block.split("\n")
    list_items = []
    for item in lines:
        if not item.startswith("*") and not item.startswith("-"):
            raise ValueError("Invalid list item")
        line_content = item[2:].lstrip("*").lstrip("-").strip()
        line_child_nodes = text_to_children(line_content)
        list_items.append(ParentNode("li", line_child_nodes))
    
    return ParentNode("ul", list_items)

def block_to_olist(block):
    lines = block.split("\n")
    list_items = []
    for item in lines:
        contents = item.split(". ", 1)
        if len(contents) <2:
            raise ValueError("Invalid ordered list item")
        if not contents[0].isdigit():
            raise ValueError("Invalid list item")
        line_content = contents[1].strip()
        line_child_nodes = text_to_children(line_content)
        list_items.append(ParentNode("li", line_child_nodes))
    
    return ParentNode("ol", list_items)

def block_to_code(block):
    code_content = block[4:-3]
    node = TextNode(code_content, "text")
    html_node = text_node_to_html_node(node)
    code_node = ParentNode("code", [html_node])
    
    return ParentNode("pre", [code_node])
    
#Helper function that takes a string and returns a list of HTMLNodes representing the inline markdown
def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_node_objects = []
    for node in nodes:
        html_node_objects.append(text_node_to_html_node(node))
    
    return html_node_objects


#Convert full markdown document into a single parent HTMLNode
def markdown_to_html_node(markdown):
    split_blocks = markdown_to_blocks(markdown)
    
    children= []
    for block in split_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            node = block_to_heading(block)
        elif block_type == BlockType.CODE:
            node = block_to_code(block)
        elif block_type == BlockType.QUOTE:
            node = block_to_quote(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = block_to_uolist(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = block_to_olist(block)
        else:
            content = " ".join(block.split("\n"))
            child = text_to_children(content)
            node = ParentNode("p", child)
        
        children.append(node)
    
    return ParentNode("div", children)
