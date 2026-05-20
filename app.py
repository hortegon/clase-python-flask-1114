
from flask import Flask, render_template



app = Flask(__name__)



@app.route("/")
def inicio():
    
    titulo = "FLASK"
    usuario = "ALEXANDER CANO"
    mensaje = "BIENVENIDOS A MI PAGINA"
   
    return render_template("index.html",
                           titulo=titulo,
    usuario=usuario,
    mensaje=mensaje)




@app.route("/MUSICA")
def musica():
   
    return render_template("MUSICA.html")


@app.route("/LOGIN")
def login():
   
    return render_template("LOGIN.html")



@app.route("/HOLA")
def hola():
   
    return render_template("HOLA.html")


@app.route("/acerca")
def acerca():
    return render_template("template/acerca.html")


@app.route("/contacto")
def contacto():
    return render_template("template/CONTACTO.html")




if __name__ == "__main__":
   
   
    app.run(debug=True)
