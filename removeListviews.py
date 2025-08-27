import sys
import xml.etree.ElementTree as ET
import logging

from termcolor import colored
import argparse


#functions -----------------------------------------
def colored_print(text, color):
  print(colored(text, color))
def printRootChildren(color):
    # Iterate over all elements that are children of the root node
    for child in root:
        # Do something with each child element
        colored_print(child.tag, color)
#--------------------------------------------------

#params -------------------------------------------


parser = argparse.ArgumentParser()
parser.add_argument("--debug", type=str, default="false", help="debug to console, default is false")
parser.add_argument("-d", type=str, default="false", help="debug to console, default is false")

parser.add_argument("--filename", type=str, help="xml file")
parser.add_argument("-f", type=str, help="xml file")

parser.add_argument("-n", default="listViews", type=str, help="node to find, default is listViews")
parser.add_argument("--node_to_find", default="listViews",type=str, help="node to find, default is listViews")

parser.add_argument("-o", type=str, help="file to output, if not supplied it will use the filename")
parser.add_argument("--output", type=str, help="file to output, if not supplied it will use the filename")
outputFile = None
NODE_TO_FIND = None
file_name = None

args = parser.parse_args()

if args.f is not None:
    file_name = args.f
if args.filename is not None:
    file_name = args.filename

if file_name is None:
    colored_print("no xml file name supplied, use -f or --filename", "red")
    exit()

#if args.n is not None:
NODE_TO_FIND = args.n
#if args.node_to_find is not None:
    #NODE_TO_FIND = args.node_to_find

if args.debug is not None:
    debug = args.debug
if args.d is not None:
    debug = args.d
    
if args.o is not None:
    outputFile = args.o
if args.output is not None:
    outputFile = args.output
if outputFile is None:
    outputFile = file_name

#--------------------------------------------------

#INPUTFILE = "objects/" + file_name + ".object"
INPUTFILE = file_name
#INPUTFILE = file_name
colored_print("Opening fie - " + INPUTFILE, "yellow")
# Parse the XML file
tree = ET.parse(INPUTFILE)
root = tree.getroot()

#printRootChildren("cyan")

# Find all <listViews> elements
NODE_TO_FIND = "{http://soap.sforce.com/2006/04/metadata}" + NODE_TO_FIND
elements = root.findall(NODE_TO_FIND)

# delete the first level of children, then look for the children of the children
for element in elements:
    root.remove(element)

for child in root:
    for c2 in child:
        if c2.tag == NODE_TO_FIND:
            #found = True
            colored_print("remove " + NODE_TO_FIND + " from child " + child.tag, "yellow")
            child.remove(c2)

    
#if bool(found) == False:
   # colored_print("No elements called '" + NODE_TO_FIND + "' found.", "red")
    #exit()
#output = file_name+".object"
output = outputFile
colored_print("Writing to " + output, "yellow")

xml_string = ET.tostring(root).decode()
xml_string = xml_string.replace("ns0:", "")
xml_string = xml_string.replace("ns0=", "")
xml_string = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+xml_string
xml_string = xml_string.replace("xmlns:", "xmlns=")
if debug == "t" or debug == "true":
    colored_print(xml_string, "green")

with open(output, "w") as file:
    file.write(xml_string)
