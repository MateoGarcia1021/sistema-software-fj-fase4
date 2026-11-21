# cliente.py
# Clase Cliente con encapsulacion y validaciones.

from entidad import EntidadBase
from excepciones import DatoInvalidoError


class Cliente(EntidadBase):
    """Representa un cliente de Software FJ con datos encapsulados."""

    def __init__(self, codigo, documento, nombre, correo):
        try:
            super().__init__(codigo)
        except ValueError as err:
            # Encadenamos el error original con nuestra excepcion personalizada.
            raise DatoInvalidoError("Codigo de cliente invalido.") from err

        # Usamos las propiedades para aplicar validaciones desde el inicio.
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        texto = str(valor).strip() if valor is not None else ""
        if len(texto) < 5:
            raise DatoInvalidoError("El documento debe tener al menos 5 caracteres.")
        self._documento = texto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        texto = str(valor).strip() if valor is not None else ""
        if len(texto) < 2:
            raise DatoInvalidoError("El nombre del cliente es muy corto o esta vacio.")
        self._nombre = texto

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        texto = str(valor).strip() if valor is not None else ""
        if "@" not in texto or "." not in texto:
            raise DatoInvalidoError("El correo electronico no es valido.")
        self._correo = texto

    def resumen(self):
        return f"Cliente [{self.codigo}] {self._nombre} | Doc: {self._documento} | Correo: {self._correo}"
