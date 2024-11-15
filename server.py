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

