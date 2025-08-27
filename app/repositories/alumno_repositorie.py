from app import db
from app.models.alumno import Alumno

class AlumnoRepository:
    @staticmethod
    def buscar_por_legajo(nro_legajo: int) -> Alumno | None:
        return db.session.query(Alumno).filter_by(nroLegajo=nro_legajo).first()
