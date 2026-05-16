
EVIDENCIA DE ENTREGA - TAREA 2 (DATOS DINÁMICOS EN FLASK)
============================================================

1. VERIFICACIÓN VISUAL:
   El servidor Flask se encuentra corriendo con éxito en http://127.0.0.1:5000.
    
   Se adjunta la captura de pantalla donde se observa el backend inyectando 
   y retornando los datos de forma dinámica .![![alt text](image-1.png)](image.png)
![![![alt text](image-3.png)]]
2. VARIABLES REQUERIDAS IMPLEMENTADAS:
   * Variable 1: `nombre` -> Tipo: Texto (Contenido: "Gabriela Garcia")
   * Variable 2: `rol`    -> Tipo: Texto (Contenido: "Administrador")
   * Variable 3: `alertas` -> Tipo: Número entero (Contenido: 4)

   ![![![alt text](image-4.png)]]

3. RESPUESTAS DE REFLEXIÓN TÉCNICA:

        ¿Qué cambia en la plantilla? Los datos dejan de ser fijos en el código visual; el archivo se vuelve una estructura moldeable que renderiza contenidos variables según las instrucciones recibidas desde el servidor en Python.

        ¿Qué ventaja tiene separar la lógica? Permite trabajar bajo el principio de separación de responsabilidades. Se puede modificar el diseño o maquetación del HTML sin alterar el procesamiento matemático o las consultas de datos en Python.
        
        ¿Qué pasa si una variable no se envía? Jinja2 / Flask manejan el error de manera silenciosa en producción, omitiendo el renderizado del marcador de posición sin detener el servidor ni lanzar pantallas de error críticas.
