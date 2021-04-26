from fabricas import *

opcion = input("Digite marca de computador para comprar \n")

# fabricas = FabricaJson()
fabricas = FabricaXml()
pc = fabricas.crearPC()
# pc.readFile()
pc.readFile(marca=opcion)
pc.readFilePartes(partes=opcion)