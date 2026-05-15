# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("index.html")


@app.route("/musica")
def musica():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("musica.html")

@app.route("/futbol")
def futbol():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("futbol.html")


@app.route("/Ropa")
def Ropa():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("Ropa.html")

@app.route("/contacto")
def contacto():
    return render_template("template/contacto.html")

@app.route("/acerca")
def acerca():
    return render_template("template/acerca.html")


# Este bloque se ejecuta solo si corremos `python app.py` desde la terminal.
if __name__ == "__main__":
    # `debug=True` sirve en desarrollo porque reinicia el servidor
    # cuando detecta cambios y muestra errores con mas detalle.
    app.run(debug=True)
