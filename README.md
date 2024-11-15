# Evaluaci&#243;n U2 y 3 de Temas
En este programa que se est&#225; alojando, se estar&#225; evaluando con la ayuda de GitHub Actions. 

Este programa se ejecuta de forma local utilizando el siguiente c&#243;digo en Python:
```py
import http.server
import socketserver

# Configuración del puerto y el manejador
PORT = 8000  # Puedes cambiar el puerto si lo deseas
Handler = http.server.SimpleHTTPRequestHandler

# Crear el servidor y especificar el puerto
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor iniciado en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener el servidor")
    httpd.serve_forever()

```
Este bloque de c&#243;digo permite crear un peque&#241;o servidor local utilizando un archivo **index.html** que debe estar en la misma carpeta donde se ejecuta el servidor.

# Informacion sobre el programa
A continuaci&#243;n, se encuentran los enlaces a los repositorios de cada elemento que forma parte del programa y su funcionamiento:

- **Pagina Web:** [Repositorio del sitio web](https://github.com/NinjaDiaz007/Proyecto_IA.git)
- **Inteligencia Aetificial:** [Repositorio de la IA](https://github.com/keyemsi/proyectoiapython.git)
