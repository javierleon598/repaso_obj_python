from flask import Flask, render_template
from fabricas import *
from random import choice

app = Flask(__name__)

@app.route('/')
def principal():
    fabricas = [FabricaHumanos(), FabricaOrcos(), FabricaElfos()]
    fabrica = choice(fabricas)
    print(type(fabrica))
    if type(fabrica) == FabricaHumanos:
        decorador = DecoradorHumanos(fabrica)
    if type(fabrica) == FabricaOrcos:
        decorador = DecoradorOrcos(fabrica)
    if type(fabrica) == FabricaElfos:
        decorador = DecoradorElfos(fabrica)


    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    cuerpo = decorador.crear_cuerpo()
    montura = decorador.crear_montura()

    productos = []

    productos.append(arma)
    productos.append(escudo)
    productos.append(cuerpo)
    productos.append(montura)

    return render_template("productos.html", productos = productos)

if __name__ == '__main__':
    app.run(debug=True)
