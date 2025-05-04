from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    ubicacion = db.Column(db.String(50), nullable=False)
    presupuesto = db.Column(db.Float, nullable=False)
    id_jefe = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=True)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(15))
    correo = db.Column(db.String(100), unique=True)
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))
    id_jefe = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=True)
