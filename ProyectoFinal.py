from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta básica
@app.route('/')
def inicio():
    return '<h1>¡Servidor web funcionando!</h1><p>Este es un servidor web básico creado con Flask.</p>'

# Ruta adicional de ejemplo
@app.route('/saludo')
def saludo():
    return '<h1>Hola desde Flask!</h1><p>Esta es otra ruta del servidor.</p>'

# Ejecutar el servidor
if __name__ == '__main__':
    print("Iniciando web...")
    print("Abre tu navegador en: http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)
