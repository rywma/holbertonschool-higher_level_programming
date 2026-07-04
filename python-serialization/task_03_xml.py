#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into XML and save it to filename.

    Args:
        dictionary (dict): the data to serialize, as key/value pairs.
        filename (str): the path of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Read XML data from filename and return it as a dictionary.

    Args:
        filename (str): the path of the input XML file.

    Returns:
        dict: the reconstructed dictionary from the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
