from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []

# pagina de inicio
@app.route("/")
def index():
    return render_template('index.html')

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