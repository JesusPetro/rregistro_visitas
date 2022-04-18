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

    # validamos la existencia del correo en la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM visitantes')
    visitantes = cur.fetchall()
    cur = mysql.connection.cursor()
    for visitante in visitantes:
        if e_mail==visitante[3]:
            cur.execute("INSERT INTO visitas (email, fecha ) VALUES (%s,%s)",(e_mail, dia))
            mysql.connection.commit()
            flash('Visita registrada satisfactoriamente')
            return redirect(url_for('index'))
        else:
            msj_error=1

    flash('Visita no registrada: el correo ingresado no se encuentra registrado como visitante ')
    return render_template('index.html',msj_error=msj_error)



    

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

    # validamos de que no se ingrese un correo ya existente en la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM visitantes')
    visitantes = cur.fetchall()
    cur = mysql.connection.cursor()
    for visitante in visitantes:
        if e_mail==visitante[3]:
            flash('El correo ingresado ya esta ascociado a otro visitante, porfavor usar otro ')
            return render_template('info_visitante.html')
            
    tipo = request.form['tipo']
    placa = request.form['placa']
    descripcion = request.form['descripcion']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO visitantes (nombre, apellido, email, tipo_visitante, placa_vehiculo, descripcion_vehiculo ) VALUES (%s,%s,%s,%s,%s,%s)", (nombre, apellido, e_mail, tipo, placa, descripcion))
    mysql.connection.commit()
    flash('Visitante agregado satisfactoriamente')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
