from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import urllib

app = Flask(__name__)

# Conexión a SQL Server
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=NTBK-5CD151509G\\SQLEXPRESS;"
    "DATABASE=dundermifflin;"
    "Trusted_Connection=yes;"
)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Departamento(db.Model):
    __tablename__ = 'Departamentos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100))
    presupuesto = db.Column(db.Float)
    id_jefe = db.Column(db.Integer, db.ForeignKey('Empleados.id'))

class Empleado(db.Model):
    __tablename__ = 'Empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(100))
    id_departamento = db.Column(db.Integer, db.ForeignKey('Departamentos.id'))
    id_jefe = db.Column(db.Integer, db.ForeignKey('Empleados.id'))

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

# Rutas
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

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)