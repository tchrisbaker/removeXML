from termcolor import colored
def colored_print(text, color):
  print(colored(text, color))
def printRootChildren(color, root):
    # Iterate over all elements that are children of the root node
    for child in root:
        # Do something with each child element
        colored_print(child.tag, color)