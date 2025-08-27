from typing import Optional
from app.models.alumno import Alumno
from app.repositories.alumno_repository import AlumnoRepository

class AlumnoService:
    @staticmethod
    def obtener_ficha_alumno(nro_legajo: int) -> Optional[Alumno]:
        return AlumnoRepository.buscar_por_legajo(nro_legajo)
