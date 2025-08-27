from weasyprint import HTML, CSS
from app.exporters.alumno_exporter import AlumnoExporter
from app.models.alumno import Alumno
import io

class AlumnoPDFExporter(AlumnoExporter):
    def exportar(self, alumno: Alumno) -> bytes:
        # Creo un HTML simple
        html_content = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: sans-serif; }}
                h1 {{ text-align: center; }}
                p {{ margin: 5px 0; }}
            </style>
        </head>
        <body>
            <h1>Ficha del Alumno</h1>
            <p><strong>Legajo:</strong> {alumno.nroLegajo}</p>
            <p><strong>Nombre:</strong> {alumno.apellido}, {alumno.nombre}</p>
            <p><strong>Documento:</strong> {alumno.tipoDocumento.nombre} {alumno.nroDocumento}</p>
            <p><strong>Fecha de Nacimiento:</strong> {alumno.fechaNacimiento.strftime('%Y-%m-%d')}</p>
            <p><strong>Sexo:</strong> {alumno.sexo}</p>
            <p><strong>Fecha de Ingreso:</strong> {alumno.fechaIngreso.strftime('%Y-%m-%d')}</p>
            <p><strong>Facultad:</strong> {alumno.facultad.nombre if alumno.facultad else '-'}</p>
        </body>
        </html>
        """

        pdf_bytes = HTML(string=html_content).write_pdf()
        return pdf_bytes
