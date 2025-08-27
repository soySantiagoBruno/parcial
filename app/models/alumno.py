from datetime import date
from app import db
from app.models.tipo_documento import TipoDocumento
from app.models.facultad import Facultad

class Alumno(db.Model):
    __tablename__ = "alumnos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apellido = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    nroDocumento = db.Column(db.String(20), nullable=False)
    tipoDocumento_id = db.Column(db.Integer, db.ForeignKey("tipo_documento.id"), nullable=False)
    tipoDocumento = db.relationship("TipoDocumento")
    fechaNacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    nroLegajo = db.Column(db.Integer, unique=True, nullable=False)
    fechaIngreso = db.Column(db.Date, nullable=False)

    facultad_id = db.Column(db.Integer, db.ForeignKey("facultades.id"))
    facultad = db.relationship("Facultad")