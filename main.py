from flask import Flask, render_template, request
import forms
from flask import flash
from flask_wtf.csrf import CSRFProtect
from wtforms import validators
from flask import g



app = Flask(__name__)
app.secret_key = "esta es mi clave secreta"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = 'Mario'
    print("Before 1")

@app.after_request
def after_request(response):
    print("after 3")
    return response




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
    print("Alumno: {}".format(g.nombre))
    alumno_clase = forms.UserForm(request.form)
    nom = ''
    apa = ''
    ama = ''
    edad = '' 
    email = ''
    if request.method == 'POST' and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.aPaterno.data
        ama = alumno_clase.aMaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data
        print("Nombre: {}".format(nom))
        print("A Paterno: {}".format(apa))
        print("A Materno: {}".format(ama))
        print("Edad: {}".format(edad))
        print("Email: {}".format(email))

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("Alumnos.html", form = alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

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