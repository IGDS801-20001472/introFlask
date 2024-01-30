from wtforms import StringField, TelField, IntegerField, EmailField, Form

class UserForm(Form):
    nombre = StringField('nombre')
    email = EmailField('email')
    aPaterno = TelField('apaterno')
    aMaterno = TelField('amaterno')
    edad  = IntegerField('edad')