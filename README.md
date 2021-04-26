# REPASO OBJETOS

## PATRONES DE DISEÑO APLICADOS

- En el ejercicio de catalogo de personajes se aplico el patron creacional Abstract Factory ya que se crean familias de objetos que dependen entre sí, sin especificar sus clases concretas como es el caso de la clase Producto que hereda a Arma, Escudo y en el otro caso de la clase Fabrica. que hereda a FabricaHumanos y FabricaOrcos.

- Tambien se implemento el patron estructural Decorator puesto que la clase Producto hereda a subclases y estas a su vez a clases hijas, como es el caso de Producto que hereda a la clase Escudo y está a la clase EscudoHumano y EscudoOrco y tambien hereda a la Arma y esta a su vez hereda a ArmaHumanos y ArmaOrcos.


## PRINCIPIOS DE DISEÑO APLICADOS:

- Don’t Repeat Yourself: se aplica en el momento que se reutiliza codigom se aplica la herencia en nuestras clases.

- S Single Responsibility: Se aplica en las clases Producto y Fabrica ya que se encargan de una sola responsabilidad.

- O Open/Closed: Se aplica puesto que el diseño de la clase Producto esta abierto a crear una extensión de dicha clase y no una modificación.

- L Liskov Substitution: Se aplica ya que clases  pueden usar las clases derivadas de estas aplicando la herencia como es el caso de Fabrica con los métodos de crear_arma, crear_escudo, crear_cuerpo, crear_montura al usar estos metodos se puede tener diferentes comportamientos.


# EXAMPLE MVC DAO

- Javier Hernández León
- David Lancheros