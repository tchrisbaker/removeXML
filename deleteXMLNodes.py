from coloredPrint import colored_print
def deleteNodes(root, NODE_TO_FIND):
    NODE_TO_FIND = "{http://soap.sforce.com/2006/04/metadata}" + NODE_TO_FIND
    print("Looking for " + NODE_TO_FIND)
    elements = root.findall(NODE_TO_FIND)
    # delete the first level of children, then look for the children of the children
    for element in elements:
        print("removing " + element.tag)
        root.remove(element)

    for child in root:
        print("checking child " + child.tag)
        for c2 in child:
            print("checking grandchild " + c2.tag)
            if c2.tag == NODE_TO_FIND:
                #found = True
                colored_print("remove " + NODE_TO_FIND + " from child " + child.tag, "yellow")
                child.remove(c2)
    return root