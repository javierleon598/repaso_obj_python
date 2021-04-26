import json
import xmltodict
# import xml.etree.ElementTree as ET
# from xml.dom import minidom
from abc import ABC, abstractmethod

class DAOJson:

    @abstractmethod
    def readFile(self):
        with open('./file/data.json') as json_data:
            json_parsed = json.loads(json_data.read())
        print(json.dumps(json_parsed, indent=4, sort_keys=True))

class DAOXml:

    @abstractmethod
    def readFile(self):
        with open('./file/data.xml') as xml_data:
            xml_parsed = xmltodict.parse(xml_data.read())
        print(xml_parsed['root']['row'])
