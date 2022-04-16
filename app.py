from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'registro_acceso_vehicular'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# pagina de inicio
@app.route("/")
def index():
    return render_template('index.html')

# registro de visitas
@app.route("/add_visita", methods=['POST'])
def add_visita():
    e_mail = request.form['e-mail']
    dia = request.form['dia']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO visitas (e-mail, fecha ) VALUES (%s,%s)",(e_mail, dia))
    mysql.connection.commit()
    flash('Visita registrada satisfactoriamente')
    return redirect(url_for('index'))

# pasamos a asolicitar los datos del visitante 
@app.route("/info_visitante")
def info_visitante():
    return render_template('info_visitante.html')


# añadimos los visitantes a la base de datos 
@app.route("/add_visitante", methods=['POST'])
def add_visitante():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    e_mail = request.form['e-mail']
    tipo = request.form['tipo']
    placa = request.form['placa']
    descripcion = request.form['descripcion']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO visitantes (nombre, apellido, e-mail, tipo visitante, placa vehiculo, descripcion vehiculo ) VALUES (%s,%s,%s,%s,%s,%s)", (nombre, apellido, e_mail, tipo, placa, descripcion))
    mysql.connection.commit()
    flash('Visitante agregado satisfactoriamente')
    return redirect(url_for('index'))
"""
@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)
"""


if __name__ == '__main__':
    app.run(debug=True)
