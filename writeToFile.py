from coloredPrint import colored_print
import xml.etree.ElementTree as ET
def writeToFile(root, outputFile, debug = False):
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