from Flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy

class usuario(db.Model):
    __tablename__= 'usuarios'

    id = db.Column(db.integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.Sctring(256), nullable=False)



class Tarea(db.model):
    __tablename__ = 'tarea'

    id = db.Column(db.integer, primary_key=True)
    titulo = db.Column(db.Strimg(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.uttenow)
    fecha_vencimiento = db.Column(db.DateTime, nullable=False)
    completada = db.Column(db.Boolean, default=False)
    prioridad = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integre, db.Foreign_key('usuarios.id'), nullable=False)
