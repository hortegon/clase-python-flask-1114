# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.


@app.route("/")
def inicio():

      return render_template("index.html")


@app.route("/index")
def index():
    
    return render_template("index.html")




@app.route("/HOLA")
def HOLA():
    
    return render_template("HOLA.html")


@app.route("/CONTACTO")
def CONTACTO():
    
    return render_template("CONTACTO.html")



@app.route("/NS")
def NS():
    
    return render_template("NS.html")



@app.route("/PERSONA")
def PERSONA():
    
    return render_template("PERSONA.html")

@app.route("/acerca")
def acerca():
    
    return render_template("acerca.html")

@app.route("/contacto")
def contacto():
    
    return render_template("contacto.html")







@app.route("/recursos")
def recursos():

    
 recursos = [
    "Git Hub",
    "Git Bash",
    "Paginas HTML",
    "Variables Jinja"
]
 return render_template("recursos.html", recursos=recursos)




if __name__ == "__main__":
   
    app.run(debug=True)
