from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Variables dinámicas para la página de inicio
    usuario_nombre = "Gabriela Garcia"
    usuario_rol = "Administrador"
    alertas_pendientes = 4
    
    return render_template(
        "index.html", 
        nombre=usuario_nombre, 
        rol=usuario_rol, 
        alertas=alertas_pendientes
    )

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route('/recursos')
def recursos():
    # Paso 2: Definir la lista en Python (mínimo 4 elementos)
    lista_recursos = [
        "🚀 Mi Entorno Virtual Configurado",
        "Rutas en Flask",
        "Plantillas HTML",
        "Variables con Jinja",
        "Bucle For en Jinja"
    ]
    # Paso 3: Enviar la lista a la plantilla
    return render_template("recursos.html", recursos=lista_recursos)

if __name__ == "__main__":
    app.run(debug=True)
