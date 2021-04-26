import json
import xmltodict
from abc import ABC, abstractmethod

class DAOJson:

    @abstractmethod
    def readFile(self, **args):
        with open('./file/data.json') as json_data:
            json_parsed = json.loads(json_data.read())
            for p in json_parsed:
                if p['computador']['marca'] == args['marca']:
                    print(p['computador']['descripcion'], ', File: JSON')

    @abstractmethod
    def readFilePartes(self, **args):
        with open('./file/data.json') as json_data:
            json_parsed = json.loads(json_data.read())
            for p in json_parsed:
                if p['computador']['marca'] == args['partes']:
                    print(p['partes']['memoria'], p['partes']['procesador'], p['partes']['board'] , ', File: JSON')

class DAOXml:

    @abstractmethod
    def readFile(self, **args):
        with open('./file/data.xml') as xml_data:
            xml_parsed = xmltodict.parse(xml_data.read())
            for elem in xml_parsed['root']['row']:
                if str(elem['computador']["marca"]) == args["marca"]:
                    print(elem['computador']['descripcion'], ', File: XML')

    @abstractmethod
    def readFilePartes(self, **args):
        with open('./file/data.xml') as xml_data:
            xml_parsed = xmltodict.parse(xml_data.read())
            for elem in xml_parsed['root']['row']:
                if str(elem['computador']["marca"]) == args["partes"]:
                    print(elem['partes']['memoria'], elem['partes']['procesador'], elem['partes']['board'] , ', File: XML')

