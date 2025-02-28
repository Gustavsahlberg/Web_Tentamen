from flask import Flask
from models import db, seedData, user_datastore, Contact, Product
from flask_migrate import Migrate, upgrade
from flask import  render_template
from flask_security import Security
from forms import ContactForm

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

security = Security(app, user_datastore)

@app.route("/", methods=["GET"])
def startSida():
    return render_template('startsida.html')

@app.route("/Contact", methods=['GET', 'POST'])
def contactUs():
    form = ContactForm()
    if form.validate_on_submit():
        if form.email.data == "" and form.telefon.data == "":
            return render_template("fel.html", felmedellande="Du måste skicka med antingen telefonnummer eller mail!")
        elif len(form.contact_msg.data) >= 512:
            return render_template("fel.html", felmedellande="För långt medelande, Max 512 chars")
        nyKontakt = Contact()
        nyKontakt.ContactName = form.name.data
        if form.email.data == "":
            nyKontakt.ContactTelefon = form.telefon.data
        elif form.telefon == "":
            nyKontakt.ContactMail = form.email.data

        nyKontakt.ContactÄrende = form.välj_ärende.data
        nyKontakt.ContactMsg = form.contact_msg.data
        db.session.add(nyKontakt)
        db.session.commit()
        return render_template("tack.html")
    
    return render_template('contact.html',form=form)


@app.route("/Products")
def products():
    alla_produkter = Product.query.all()
    return render_template("products.html",alla_produkter=alla_produkter)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
    app.run()


