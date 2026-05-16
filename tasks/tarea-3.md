# Tarea 3 - Crear varias rutas y varias paginas en Flask

## Preparación
 1.   Ejecuta la app con python app.py.
 2.   Verifica que `http://127.0.0.1:5000/` responda correctamente.
 ![alt text](image-5.png)
 3.   Ten abierto app.pyy la carpeta templates/.
Guía paso a paso



## Guía paso a paso

Paso 2 y 3: Crear la ruta/acerca y contacto
![alt text](image-6.png)


Paso 4: Crear las plantillas nuevas

Crea dos archivos:

1. templates/acerca.html
2. templates/contacto.html
Cada archivo debe tener estructura HTML básica y un título visible (h1) para distinguir la página.

![alt text](image-7.png)


Paso 5: Agregar navegación entre páginas
![alt text](image-8.png)

## Lista de verificación de validación

1. app.pycontiene /, /acercay /contacto.
2. Existen `index.html`, `acerca.html` y `contacto.html`.
3. Las tres paginas cargan sin error.
4. Hay navegación entre las tres rutas.

`index.html` 
![alt text](<Captura de pantalla 2026-05-15 220322.png>)

`acerca.html`
![alt text](<Captura de pantalla 2026-05-15 220423.png>)

`contacto.html`
![alt text](<Captura de pantalla 2026-05-15 220345.png>)


## Preguntas de reflexion tecnica
*Que parte define la URL pública: el nombre de la función o @app.route(...)?

    ¿Qué parte define la URL pública?La define exclusivamente el decorador @app.route(...). El texto entre comillas dentro de los paréntesis especifica la dirección exacta que el usuario debe escribir en el navegador.

*Si cambias el nombre de la función, ¿que debes mantener para no romper la URL?

    ¿Qué debes mantener si cambias el nombre de la función?Debes mantener intacto el decorador @app.route(...) justo arriba de la función. El nombre de la función de Python es interno, pero el decorador es el que la vincula con la URL pública.

*¿Por qué separar cada sección en su propia plantilla para mejorar el proyecto?

    Mejora el proyecto por tres razones clave:

    * Orden: Evita tener un solo archivo gigante y confuso. 

    *Mantenimiento: Si falla la página de contacto, solo 
      modificas contacto.html sin riesgo de romper el inicio.
    
    *Reutilización: Permite usar herramientas avanzadas de Flask 
      (como la herencia de plantillas con {% extends %}) para no 
      repetir el mismo menú de navegación en todos los archivos.
