from abc import ABC, abstractmethod
from app.models.alumno import Alumno

class AlumnoExporter(ABC):
    @abstractmethod
    def exportar(self, alumno: Alumno):
        pass
