from abc import ABC, abstractmethod
from dao import *

class FabricaAbstracta(ABC):

    @abstractmethod
    def crearPC(self):
        pass

class FabricaJson(FabricaAbstracta):

    def crearPC(self):
        return DAOJson()

class FabricaXml(FabricaAbstracta):

    def crearPC(self):
        return DAOXml()
