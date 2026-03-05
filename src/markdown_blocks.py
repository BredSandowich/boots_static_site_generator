from enum import Enum

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