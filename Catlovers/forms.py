from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    Ärende = ["Support", "Försäljning","Samarbeten", "Övrigt"]
    name = StringField("Name", validators=[DataRequired(),Length(min=2,max=50)])
    email = EmailField("Email", validators=[Length(max=50, message="maximum 50 char"), Optional()])
    telefon = StringField("Telefonnummer:", validators=[ Length(min=5, max=15), Optional()])
    välj_ärende = SelectField("Ärende:",choices=Ärende, validators=[DataRequired()])
    contact_msg = StringField("Kontakt medelande", validators=[DataRequired(),Length(max=512, message="maximum 512 chars")], widget=TextArea())
    submit = SubmitField("Contact")

