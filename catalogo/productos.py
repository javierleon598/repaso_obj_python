class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "Arma de los humanos"

class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "Arma de los orcos"

class ArmaElfos(Arma):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/arma.png"
        self.descripcion = "Arma de los elfos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Escudo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "Escudo de los humanos"

class EscudoOrcos(Escudo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "Escudo de los orcos"

class EscudoElfos(Escudo):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/escudo.png"
        self.descripcion = "Escudo de los elfos"


class Cuerpo(Producto):
    def __init__(self):
        Producto.__init__(self)        

class CuerpoHumanos(Cuerpo):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/cuerpo.png"
        self.descripcion = "Cuerpo de los humanos"

class CuerpoOrcos(Cuerpo):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/cuerpo.png"
        self.descripcion = "Cuerpo de los orcos"

class CuerpoElfos(Cuerpo):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/cuerpo.png"
        self.descripcion = "Cuerpo de los elfos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)        

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = "Humanos"
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "Montura de los humanos"

class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = "Orcos"
        self.imagen = "imagenes/orcos/montura.png"
        self.descripcion = "Montura de los orcos"

class MonturaElfos(Cuerpo):
    def __init__(self):
        self.grupo = "Elfos"
        self.imagen = "imagenes/elfos/montura.png"
        self.descripcion = "Montura de los elfos"      