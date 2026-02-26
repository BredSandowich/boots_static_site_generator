from textnode import TextType, TextNode, text_node_to_html_node

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