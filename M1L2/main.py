import http.server
import socketserver
import webbrowser
import os

# Cambia esta ruta por la carpeta donde está tu HTML, CSS, imágenes, etc.
directorio = r"C:\Users\Jose Antonio\OneDrive\Escritorio\Python Proyectos After M3L1\CLASES CSS\M1L2"
os.chdir(directorio)

# Configuraciones del servidor
puerto = 8000

# Iniciar servidor HTTP
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", puerto), Handler) as httpd:
    print(f"Servidor corriendo en http://localhost:{puerto}")
    webbrowser.open(f"http://localhost:{puerto}/")  # Abre el navegador automáticamente
    httpd.serve_forever()