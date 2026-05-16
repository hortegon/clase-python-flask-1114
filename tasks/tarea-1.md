# Tarea 1 - Levantar una aplicacion Flask desde cero

## Objetivo tecnico

Poner en marcha el proyecto en tu entorno local, entender para que sirve cada pieza minima del setup y verificar que la aplicacion responde en el navegador.

En esta primera clase no alcanza con "hacerlo andar". Tienes que empezar a distinguir que problema resuelve cada paso: aislamiento del entorno, instalacion de dependencias, arranque del servidor y renderizado de una plantilla HTML.

## Preparacion

Para instalar dependencias y ejecutar el proyecto, sigue el `README.md`.

## Consigna

1. Instala las dependencias y levanta la aplicacion siguiendo el `README.md`.

2. Abre la aplicacion en el navegador y comprueba que responde correctamente.

3. Modifica la vista base y verifica el cambio:

   Edita `templates/index.html`, cambia al menos el `<title>` y el `<h1>`, guarda y recarga la pagina.

![alt text](<Captura de pantalla 2026-05-07 140938.png>)

   Este paso existe para que veas la relacion concreta entre archivo fuente, servidor y resultado en navegador. Codigo que no observas, no lo entendes.

## Preguntas de reflexion tecnica

1. Que problema concreto resuelve el entorno virtual en un proyecto Python?

       Evita el "conflicto de dependencias".
       Si un proyecto A necesita la versión 1.0 de una librería y el proyecto B necesita la 2.0,
       el entorno virtual permite que ambos convivan en la misma máquina sin romperse entre sí.

2. Que diferencia hay entre instalar `Flask` globalmente y hacerlo dentro de `.venv`?

       Instalarlo globalmente ensucia tu sistema operativo y obliga a que todos tus proyectos usen la misma versión.
       En .venv, Flask es "desechable" y específico para ese proyecto, facilitando que sea portable y limpio.

3. Por que `requirements.txt` forma parte del proyecto y no de tu maquina personal?

       Es el "manual de instrucciones" de las dependencias.
       Se incluye en el proyecto para que cualquier otra persona (o un servidor en la nube)
       pueda replicar exactamente tu entorno técnico con un solo comando.
   
4. Cuando ejecutas `python app.py`, que archivo actua como punto de entrada y por que?

       El archivo que ejecutas (app.py) actúa como tal porque es el que instancia el objeto Flask
       (app = Flask(__name__)) y arranca el servidor local que escucha las peticiones.
   
5. Que relacion hay entre la ruta `/`, la funcion `inicio()` y el archivo `templates/index.html`?

       1. La relación:/ es la ruta (URL) que pide el usuario.
       2. inicio() es la función que Flask ejecuta cuando alguien llega a esa ruta.
       3. templates/index.html es el resultado visual que la función decide enviar de vuelta al navegador.

6. Que evidencia te da la terminal de que el servidor arranco correctamente?

       Verás una línea que dice algo como * Running on http://127.0.0.1:5000.
       Eso indica que el proceso está activo y esperando conexiones en esa dirección IP y puerto.

7.  Si cambias el HTML y el navegador muestra otra cosa, que te demuestra eso sobre el flujo entre backend y frontend en este proyecto?

        Demuestra que el servidor (backend) es el que sirve el contenido dinámicamente.
        Si cambias el HTML y se refleja, confirmas que el backend está leyendo el
        archivo actualizado y entregándolo correctamente al navegador (frontend) cada vez que refrescas.

## Entregable

La tarea se considera completa si puedes demostrar estas cuatro cosas:

1. El entorno virtual esta creado y activado.
![alt text](<Captura de pantalla 2026-05-07 134312.png>)

2. Las dependencias se instalaron desde `requirements.txt`.
![alt text](<Captura de pantalla 2026-05-07 134223.png>)

3. La aplicacion corre en tu maquina y responde en el navegador.
![alt text](<Captura de pantalla 2026-05-07 140439.png>)

4. Modificaste `templates/index.html` y podes señalar exactamente donde se refleja ese cambio.
![alt text](<Captura de pantalla 2026-05-07 140938.png>)

## Cierre

No estas aprendiendo a tipear comandos. Estas empezando a construir criterio tecnico. Si hoy entiendes que levanta el servidor, de donde salen las dependencias y por que Flask encuentra esa plantilla, entonces arrancaste bien. Simple no significa superficial.
