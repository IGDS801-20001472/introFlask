from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout2.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La mutiplicacion de {} * {} = {}".format(num1, num2, str(int(num1) * int(num2)))
    else:
        return '''
            <form action="/resultado" method="POST">
                <label>N1</label>
                <input type="text" name="n1"></input><br>
                <label>N2</label>
                <input type="text" name="n2"></input><br>
                <input type="submit">
            </form>
            '''

@app.route("/operabas")
def operabas():
    return render_template("operabas.html")



@app.route("/alumnos", methods = ['GET', 'POST'])
def alumnos():
    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST':
        pass

    return render_template("Alumnos.html", form = alumno_clase)

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