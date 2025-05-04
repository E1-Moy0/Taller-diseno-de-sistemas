from flask import Flask, render_template, request, redirect, url_for
from models import db, Empleado, Departamento

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dunder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('listar_empleados'))

@app.route('/empleados', methods=['GET', 'POST'])
def listar_empleados():
    if request.method == 'POST':
        nuevo = Empleado(
            nombre=request.form['nombre'],
            apellido=request.form['apellido'],
            telefono=request.form['telefono'],
            correo=request.form['correo'],
            id_departamento=request.form['id_departamento'] or None,
            id_jefe=request.form['id_jefe'] or None
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('listar_empleados'))

    empleados = Empleado.query.all()
    departamentos = Departamento.query.all()
    return render_template('empleados.html', empleados=empleados, departamentos=departamentos)

@app.route('/departamentos', methods=['GET', 'POST'])
def listar_departamentos():
    if request.method == 'POST':
        nuevo = Departamento(
            nombre=request.form['nombre'],
            ubicacion=request.form['ubicacion'],
            presupuesto=request.form['presupuesto'],
            id_jefe=request.form['id_jefe'] or None
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('listar_departamentos'))

    departamentos = Departamento.query.all()
    empleados = Empleado.query.all()
    return render_template('departamentos.html', departamentos=departamentos, empleados=empleados)

if __name__ == '__main__':
    app.run(debug=True)
