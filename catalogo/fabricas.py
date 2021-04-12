from productos import *

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

    def crear_cuerpo(self):
        pass

    def crear_montura(self):
        pass    


class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

    def crear_cuerpo(self):
        return CuerpoHumanos()

    def crear_montura(self):
        return MonturaHumanos()   

class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()

    def crear_cuerpo(self):
        return CuerpoOrcos()

    def crear_montura(self):
        return MonturaOrcos()   

class FabricaElfos(Fabrica):
    def crear_arma(self):
        return ArmaElfos()

    def crear_escudo(self):
        return EscudoElfos()

    def crear_cuerpo(self):
        return CuerpoElfos()

    def crear_montura(self):
        return MonturaElfos()   
