
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 
import psycopg2.extras

 
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"
 
DB_HOST = "localhost"
DB_NAME = "Proyecto_Integrador"
DB_USER = "postgres"
DB_PASS = "erick123E"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
 
@app.route('/in')
def Index():
    return render_template('index.html')
 
@app.route('/add_student', methods=['POST','GET'])
def add_student():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        nom_us1 = request.form['nom_us1']
        nom_us2= request.form['nom_us2']
        ape_us1 = request.form['ape_us1']
        ape_us2= request.form['ape_us2']
        calle_pri = request.form['calle_pri']
        calle_secu = request.form['calle_secu']
        nro_casa = request.form['nro_casa']
        parroquia = request.form['parroquia']
        telefono = request.form['telefono']
        email = request.form['email']
        password = request.form['password']
        validacion = request.form['validacion']
        id_rol = request.form['id_rol']
        if password == validacion:
            cur.execute("INSERT INTO usuarios (id_usuario,nom_us1,nom_us2,ape_us1,ape_us2,calle_pri,calle_secu,nro_casa,parroquia,telefono, correo_electronico,contraseña,validacion,id_rol) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id_usuario,nom_us1,nom_us2,ape_us1,ape_us2,calle_pri,calle_secu,nro_casa,parroquia,telefono, email,password,validacion,id_rol))
            conn.commit()
            flash('Los Datos se han guardado exitosamente')
            return render_template('loggin3.html')
        return render_template('index.html')
    return render_template('loggin3.html')     
if __name__ == "__main__":
    app.run(debug=True)
