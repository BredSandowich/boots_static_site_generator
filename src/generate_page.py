from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
import os
import shutil
from pathlib import Path

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
    
    
    #Function to generate sub pages from Markdown file recusively
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating subpages from {dir_path_content}to {dest_dir_path} using {template_path}")
        
    for filepath in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, filepath)
        destination_path = os.path.join(dest_dir_path, filepath)
        
        if os.path.isfile(source_path) and source_path.endswith(".md"):
            print(f"Generating {source_path} to {destination_path}")
            dest_path_obj = Path(destination_path).with_suffix(".html")
            generate_page(source_path, template_path, dest_path_obj)

        if os.path.isdir(source_path):
            print(f"Creating directory {destination_path}")
            generate_pages_recursive(source_path, template_path, destination_path)
