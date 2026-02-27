from textnode import TextType, TextNode, text_node_to_html_node
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            string = node.text.split(delimiter)
            if len(string)%2 == 0:
                raise Exception("Missing a closing delimiter")
            for i in range(len(string)):
                if string[i] == "":
                    continue
                else:
                    if i%2 == 0:
                        new_nodes.append(TextNode(string[i], TextType.TEXT))
                    if i%2 == 1:
                        new_nodes.append(TextNode(string[i], text_type))
    return new_nodes


#From alt text and URL for images from raw markdown text 
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

#From anchor text and URL for links from raw markdown text 
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


#Split the images
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if images == []:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue
            
            remaining_text = node.text
            for image in images:
                string_beginning = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
                if string_beginning[0] != "":
                    new_nodes.append(TextNode(string_beginning[0], TextType.TEXT))
                
                new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                remaining_text = string_beginning[1]
            
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
                    
    return new_nodes


#Split the links
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if links == []:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue
            
            remaining_text = node.text
            for link in links:
                string_beginning = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
                if string_beginning[0] != "":
                    new_nodes.append(TextNode(string_beginning[0], TextType.TEXT))
                
                new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                remaining_text = string_beginning[1]
            
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
                    
    return new_nodes