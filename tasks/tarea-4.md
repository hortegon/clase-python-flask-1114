# Tarea 4 - Mostrar listas con Jinja en Flask

## Guía paso a paso

Paso 1 al 6: 
![alt text](image-9.png)

Paso 7: Verificar en el navegador

1. Abre http://127.0.0.1:5000/recursos.
2. Comprueba que se vean los 4 (o más) elementos.
![alt text](<Captura de pantalla 2026-05-15 231917.png>)

3. Cambia un texto en la lista de app.py, guarda y recarga.
4. Verifica que el cambio aparezca en la página.
![alt text](image-10.png)


## Preguntas de reflexion tecnica

¿Que cambia entre renderizar una variable simple y renderizar una lista?

    La variable simple se inserta directamente como texto único. La lista requiere una estructura de control ({% for %}) para iterar y generar elementos HTML repetitivos dinámicamente

¿Dónde se ejecuta el bucle de Jinja: en el navegador o en Flask?

    Se ejecuta en Flask (servidor). El navegador nunca ve el código Jinja; solo recibe el HTML puro ya procesado con las etiquetas <li> construidas.

¿Qué ventaja aporta este patrón para casos reales (productos, tareas, alumnos)?

    Permite desacoplar los datos del diseño. Si la base de datos cambia (añades 100 productos o alumnos), el código HTML sigue siendo el mismo y la interfaz se actualiza sola.


## Entregable

1. `app.py` con ruta `/recursos` funcional.
2. `templates/recursos.html` creado.
3. Lista de mínimo 4 recursos definidos en Python.
4. Lista mostrada con bucle ` {% for %} `en HTML.
5. Navegacion hacia y desde la pagina de recursos.
6. Explicación corta del flujo: `lista en Python -> render_template -> bucle Jinja -> HTML final en navegador.`


### Explicación Corta del Flujo (Entregable)

1. Lista en Python: Se crea la colección de datos en memoria dentro de la función de Flask.

2. render_template: Flask toma los datos y los "inyecta" al archivo HTML como un parámetro.

3. Bucle Jinja: El motor procesa el archivo, lee el ciclo {% for %} y clona la etiqueta <li> por cada dato existente.

4. HTML Final: El servidor envía un documento HTML estándar al navegador, el cual solo se encarga de renderizar la lista visible.
