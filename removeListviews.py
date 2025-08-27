import xml.etree.ElementTree as ET
import argparse
from deleteXMLNodes import deleteNodes
from writeToFile import writeToFile
from coloredPrint import colored_print, printRootChildren

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

INPUTFILE = file_name

colored_print("Opening fie - " + INPUTFILE, "yellow")
# Parse the XML file
tree = ET.parse(INPUTFILE)
root = tree.getroot()

root = deleteNodes(root, NODE_TO_FIND)

writeToFile(root, outputFile)
