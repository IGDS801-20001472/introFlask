from wtforms import Form
from wtforms import StringField, TelField

class UserForm(Form):
    nombre = StringField('nombre')
    email = StringField('email')
    aPaterno = TelField('apaterno')