from productos import *

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

class FabricaElfos(Fabrica):
    def crear_arma(self):
        return ArmaElfos()

    def crear_escudo(self):
        return EscudoElfos()

###################################
class FabricaB:
    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass  

class Decorador(FabricaB):
    def __init__(self, fabricaB):
        self.__comp__ = fabricaB

    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass  

class DecoradorHumanos(Decorador):
    def crear_cuerpo(self):
        return CuerpoHumanos()
        self.__comp__.crear_cuerpo()

    def crear_montura(self):
        return MonturaHumanos()
        self.__comp__.crear_montura()

class DecoradorOrcos(Decorador):
    def crear_cuerpo(self):
        return CuerpoOrcos()
        self.__comp__.crear_cuerpo()

    def crear_montura(self):
        return MonturaOrcos()   
        self.__comp__.crear_montura()

class DecoradorElfos(Decorador):
    def crear_cuerpo(self):
        return CuerpoElfos()
        self.__comp__.crear_cuerpo()

    def crear_montura(self):
        return MonturaElfos()   
        self.__comp__.crear_montura()


