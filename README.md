# REPASO OBJETOS

PRINCIPIOS DE DISEÑO APLICADOS:

● S Principio de responsabilidad única – Single Responsibility Principle: Es aplicado en las clases manejadas ya que tanto la clase producto como la clase fabrica se encargan de mantener únicamente la información contenida en dichas clases.

● O abierto cerrado – open closed Principle Es aplicado ya que el diseño se plantea que para hacer un nuevo producto solo es necesario crear una extensión mas no una modificación como es el caso de la extensión de montura que únicamente se extiende a partir de una clase producto.

● L Substitución de Liskov - Liskov Substitution Principle Se aplica al heredar de una super clase con métodos abstractos como es el caso de fabrica con los métodos de crear arma, este puede tener diferentes comportamientos.

PATRONES DE DISEÑO APLICADOS

● Factory: Los objetos son creados a partir de una super clase como es el caso de la clase producto que hereda a armas, monturas escudos y cuerpos de personajes.

● Decorator: La super clase producto hereda a sub clases y estas a clases hijas, como es el caso de la clase producto que hereda a la clase escudo y está a la clase escudo humano y escudo orco.

● Comportamentales Template Method: Permite que las subclases tengan comportamientos diferentes, una subclase escudo puede heredar a una clase escudo orco y escudo humano que retornan resultados diferentes.



●
