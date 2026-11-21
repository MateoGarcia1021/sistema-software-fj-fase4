# logger.py
# Registra eventos y errores en un archivo de texto (sin base de datos).

from datetime import datetime


ARCHIVO_LOG = "eventos_software_fj.log"


def registrar_evento(nivel, mensaje):
    """Escribe una linea con fecha, nivel y mensaje en el archivo de log."""
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha_hora}] [{nivel}] {mensaje}\n"
    archivo = None

    try:
        # Abrimos en modo 'a' para ir agregando registros sin borrar los anteriores.
        archivo = open(ARCHIVO_LOG, "a", encoding="utf-8")
        archivo.write(linea)
    except OSError as err:
        # Si falla el archivo, avisamos en pantalla pero seguimos ejecutando.
        print(f"No se pudo escribir en el log: {err}")
    finally:
        # Cerramos el archivo si quedo abierto.
        if archivo is not None and not archivo.closed:
            archivo.close()
