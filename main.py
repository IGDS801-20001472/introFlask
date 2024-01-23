from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    titulo = "UTL"
    nombres = ["Mario", "Pedro", "Ulises"]
    return render_template("Alumnos.html", titulo = titulo, nombres = nombres)

@app.route("/maestros")
def maestros():
    return render_template("Maestros.html")

@app.route("/hola")
def hola():
    return "<h1>Saludos desde Hola</h1>"

@app.route("/saludo")
def saludo():
    return "<h1>Saludos desde Saludo</h1>"

@app.route("/nombre/<string:nom>")
def func(nom):
    return "Hola " + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "Numero: {}".format(n1)

@app.route("/user/<int:id>/<string:nombre>")
def usuario(id, nombre):
    return "ID: {} Nombre: {}".format(id, nombre)

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return "La suma de {} + {} = {}".format(num1, num2, num1 + num2)

if __name__ == "__main__":
    app.run(debug=True)