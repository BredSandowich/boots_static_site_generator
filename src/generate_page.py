from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
import os

#Function to generate a page
def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            split = line.split(" ", 1)
            return split[1]
    raise Exception("No H1 header found")

#Function to generate a page from Markdown file
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}to {dest_path} using {template_path}")
    
    file = open(from_path)
    path_content = file.read()
    file.close()
    
    template = open(template_path)
    template_content = template.read()
    template.close()
    
    
    node = markdown_to_html_node(path_content)
    html = node.to_html()
    
    page_title = extract_title(path_content)
    template_content = template_content.replace("{{ Title }}", page_title)
    template_content = template_content.replace("{{ Content }}", html)
    
    dest_directory = os.path.dirname(dest_path)
    if dest_directory != "":
        os.makedirs(dest_directory, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)
    to_file.close()