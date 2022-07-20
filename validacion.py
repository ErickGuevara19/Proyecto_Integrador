
from flask import Flask, render_template, request
import psycopg2 
import psycopg2.extras
from app import *
 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "Proyecto_Integrador"
DB_USER = "postgres"
DB_PASS = "erick123E"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/login')
def login():
    return render_template('loggin3.html')

@app.route('/val', methods=['POST','GET'])
def validar_usuario():
    click=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        correo_electronico1 = request.form['email1']
        contraseña1 = request.form['password1']
        
        click.execute(' Select * From usuarios where correo_electronico = %s AND contraseña = %s ' , (correo_electronico1, contraseña1))
        
        acount = click.fetchone()
    if acount:
        return render_template ('index1.html')
    else:
        return render_template ('loggin3.html')

if __name__ == "__main__":
    app.run(debug=True)
