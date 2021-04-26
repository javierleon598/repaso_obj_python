from fabricas import *

# fabricas = FabricaJson()
fabricas = FabricaXml()
pc = fabricas.crearPC()
pc.readFile()