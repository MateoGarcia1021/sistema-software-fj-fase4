# reserva.py
# Clase Reserva para gestionar reservas, estados y manejo de excepciones.

from excepciones import DatoInvalidoError, ServicioNoDisponibleError, OperacionReservaError
from logger import registrar_evento


class Reserva:
    """Integra un Cliente, un Servicio, duracion/cantidad y estado."""

    def __init__(self, codigo_reserva, cliente, servicio, cantidad):
        if not codigo_reserva or not str(codigo_reserva).strip():
            raise DatoInvalidoError("El codigo de reserva es obligatorio.")
        if cliente is None or servicio is None:
            raise DatoInvalidoError("La reserva necesita un cliente y un servicio validos.")

        self.codigo_reserva = str(codigo_reserva).strip()
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "PENDIENTE"
        self.total_calculado = 0.0

    def confirmar(self):
        if self.estado == "CANCELADA":
            raise OperacionReservaError("No se puede confirmar una reserva cancelada.")
        if not self.servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.servicio.nombre} no esta disponible.")
        self.estado = "CONFIRMADA"
        registrar_evento("INFO", f"Reserva {self.codigo_reserva} confirmada para {self.cliente.nombre}.")

    def cancelar(self, motivo="Cancelada por el usuario"):
        if self.estado == "CONFIRMADA":
            self.estado = "CANCELADA"
            registrar_evento("INFO", f"Reserva {self.codigo_reserva} cancelada. Motivo: {motivo}")
        elif self.estado == "PENDIENTE":
            self.estado = "CANCELADA"
            registrar_evento("INFO", f"Reserva pendiente {self.codigo_reserva} cancelada.")
        else:
            raise OperacionReservaError("La reserva ya estaba cancelada.")

    def procesar(self, descuento=0.0, impuesto=0.19):
        """Calcula el costo y confirma la reserva usando try/except/else/finally y encadenamiento."""
        try:
            if not self.servicio.disponible:
                raise ServicioNoDisponibleError(f"Servicio '{self.servicio.nombre}' no disponible.")

            self.total_calculado = self.servicio.calcular_costo(
                self.cantidad,
                descuento=descuento,
                impuesto=impuesto
            )
            self.confirmar()
        except (DatoInvalidoError, ServicioNoDisponibleError) as err_origen:
            registrar_evento("ERROR", f"Fallo al procesar reserva {self.codigo_reserva}: {err_origen}")
            # Encadenamos la excepcion original para conservar la causa real.
            raise OperacionReservaError(f"Error procesando reserva {self.codigo_reserva}") from err_origen
        else:
            # Solo se ejecuta si no hubo excepciones en try ni except.
            mensaje_ok = (
                f"Reserva {self.codigo_reserva} procesada con exito. "
                f"Cliente: {self.cliente.nombre}, Total: ${self.total_calculado}"
            )
            registrar_evento("INFO", mensaje_ok)
            return self.total_calculado
        finally:
            # Siempre se ejecuta al terminar el intento de procesar.
            registrar_evento("INFO", f"Intento de procesamiento finalizado para reserva {self.codigo_reserva} (Estado: {self.estado}).")
