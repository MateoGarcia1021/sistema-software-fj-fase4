# entidad.py
# Clase abstracta base para entidades generales del sistema.

from abc import ABC, abstractmethod


class EntidadBase(ABC):
    """Clase abstracta que obliga a las clases hijas a implementar resumen()."""

    def __init__(self, codigo):
        # Validamos que el codigo no venga vacio.
        if not codigo or not str(codigo).strip():
            raise ValueError("El codigo de la entidad no puede estar vacio.")
        self.codigo = str(codigo).strip()

    @abstractmethod
    def resumen(self):
        """Devuelve un texto corto con la informacion principal."""
        pass
