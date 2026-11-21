# servicios.py
# Clase abstracta Servicio y tres servicios especializados de Software FJ.

from abc import ABC, abstractmethod
from entidad import EntidadBase
from excepciones import DatoInvalidoError


class Servicio(EntidadBase, ABC):
    """Clase base abstracta para todos los servicios."""

    def __init__(self, codigo, nombre, tarifa_base, disponible=True):
        try:
            super().__init__(codigo)
        except ValueError as err:
            raise DatoInvalidoError("Codigo de servicio invalido.") from err

        if not nombre or not str(nombre).strip():
            raise DatoInvalidoError("El nombre del servicio no puede estar vacio.")
        if tarifa_base is None or tarifa_base <= 0:
            raise DatoInvalidoError("La tarifa base debe ser mayor que cero.")

        self.nombre = str(nombre).strip()
        self.tarifa_base = float(tarifa_base)
        self.disponible = bool(disponible)

    @abstractmethod
    def validar_parametros(self, cantidad):
        """Valida si la cantidad o duracion es valida para este servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve una descripcion detallada del servicio."""
        pass

    def calcular_costo(self, cantidad, descuento=0.0, impuesto=0.19):
        """Calcula el costo total. Acepta descuento e impuesto opcionales (sobrecarga por defecto)."""
        self.validar_parametros(cantidad)

        if descuento < 0 or descuento >= 1:
            raise DatoInvalidoError("El descuento debe estar entre 0 y menos de 1 (ej. 0.1 para 10%).")
        if impuesto < 0 or impuesto > 1:
            raise DatoInvalidoError("El impuesto debe estar entre 0 y 1 (ej. 0.19 para 19%).")

        subtotal_base = self._calcular_subtotal_servicio(cantidad)
        con_descuento = subtotal_base * (1 - descuento)
        total = con_descuento * (1 + impuesto)
        return round(total, 2)

    @abstractmethod
    def _calcular_subtotal_servicio(self, cantidad):
        """Calcula el subtotal segun la logica de cada tipo de servicio."""
        pass

    def resumen(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Servicio [{self.codigo}] {self.nombre} ({estado})"


class ReservaSala(Servicio):
    """Servicio para reservar salas (cantidad = horas)."""

    def __init__(self, codigo, nombre, tarifa_base, capacidad_personas, disponible=True):
        super().__init__(codigo, nombre, tarifa_base, disponible)
        if capacidad_personas <= 0:
            raise DatoInvalidoError("La capacidad de la sala debe ser mayor que cero.")
        self.capacidad_personas = int(capacidad_personas)

    def validar_parametros(self, cantidad):
        if cantidad is None or cantidad <= 0 or cantidad > 12:
            raise DatoInvalidoError("Las horas de reserva de sala deben estar entre 1 y 12.")

    def describir(self):
        return f"Reserva de sala '{self.nombre}' (capacidad: {self.capacidad_personas} personas, tarifa/hora: ${self.tarifa_base})"

    def _calcular_subtotal_servicio(self, cantidad):
        return self.tarifa_base * cantidad


class AlquilerEquipo(Servicio):
    """Servicio para alquilar equipos (cantidad = dias de alquiler)."""

    def __init__(self, codigo, nombre, tarifa_base, tipo_equipo, disponible=True):
        super().__init__(codigo, nombre, tarifa_base, disponible)
        if not tipo_equipo or not str(tipo_equipo).strip():
            raise DatoInvalidoError("Debe indicar el tipo de equipo.")
        self.tipo_equipo = str(tipo_equipo).strip()

    def validar_parametros(self, cantidad):
        if cantidad is None or cantidad <= 0 or cantidad > 30:
            raise DatoInvalidoError("Los dias de alquiler deben estar entre 1 y 30.")

    def describir(self):
        return f"Alquiler de equipo '{self.nombre}' ({self.tipo_equipo}, tarifa/dia: ${self.tarifa_base})"

    def _calcular_subtotal_servicio(self, cantidad):
        return self.tarifa_base * cantidad


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria especializada (cantidad = horas de asesoria)."""

    def __init__(self, codigo, nombre, tarifa_base, area_tema, disponible=True):
        super().__init__(codigo, nombre, tarifa_base, disponible)
        if not area_tema or not str(area_tema).strip():
            raise DatoInvalidoError("Debe indicar el area o tema de la asesoria.")
        self.area_tema = str(area_tema).strip()

    def validar_parametros(self, cantidad):
        if cantidad is None or cantidad <= 0 or cantidad > 20:
            raise DatoInvalidoError("Las horas de asesoria deben estar entre 1 y 20.")

    def describir(self):
        return f"Asesoria '{self.nombre}' en {self.area_tema} (tarifa/hora: ${self.tarifa_base})"

    def _calcular_subtotal_servicio(self, cantidad):
        # Si la asesoria supera 5 horas, se aplica un pequeno ajuste del 5% por paquete extenso.
        subtotal = self.tarifa_base * cantidad
        if cantidad > 5:
            subtotal = subtotal * 0.95
        return subtotal
