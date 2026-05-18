# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.

#tarea dos
@app.route("/")
def inicio():
    titulo = "INICIO"                 #1 VARIABLE USADA
    usuario ="STEVEN MONROY 11-14"    #2 VARIABLE USADA
    mensaje ="BIENVENIDOS A MI FLASK" #3 VARIABLE USADA

    return render_template(
        "index.html",
        titulo=titulo, 
        usuario=usuario, 
        mensaje=mensaje
    )
    
    


#tarea tres
@app.route("/contacto")
def contacto():
    return render_template("template/contacto.html")

@app.route("/acerca")
def acerca():
    return render_template("template/acerca.html")


#tarea cuatro
@app.route("/recursos")
def recursos():
    recursos = [
        "Entorno virtual",
        "Rutas en Flask",
        "Plantilla HTML",
        "Variables con JInja"
    ]

    return render_template("recursos.html", recursos=recursos)

# Este bloque se ejecuta solo si corremos `python app.py` desde la terminal.
if __name__ == "__main__":
 
    app.run(debug=True)
