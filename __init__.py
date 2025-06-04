from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"


@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
# comment tu run actions

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    resultat = valeur1 + valeur2
    parite = "pair" if resultat % 2 == 0 else "impair"
    return f"<h2>La somme de {valeur1} et {valeur2} est : {resultat}</h2><p>C'est un nombre {parite}.</p>"



                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)






