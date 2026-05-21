
from flask import Flask, render_template



app = Flask(__name__)



@app.route("/")
def inicio():

    titulo = "Panel de inicio"
    usuario = "Zury"
    mensaje = "Bienvenida a Flask"
   
    return render_template("index.html",
                             
    titulo=titulo,
    usuario=usuario,
    mensaje=mensaje)


@app.route("/contacto")
def contacto():
    return render_template("template/contacto.html")



@app.route("/HOLA")
def hola():
    return render_template("HOLA.html")


@app.route("/acerca")
def acerca():
    return render_template("template/acerca.html")


@app.route("/ADIOS")
def adios():
    return render_template("ADIOS.html")



@app.route("/LOVE")
def love():
    return render_template("LOVE.html")



@app.route("/recursos")
def recursos():
    recursos = [
    "Entorno virtual",
    "Rutas en Flask",
    "Plantillas HTML",
    "Variables con Jinja"
]
    return render_template("recursos.html",recursos=recursos)
    


if __name__ == "__main__":
    
    app.run(debug=True)
