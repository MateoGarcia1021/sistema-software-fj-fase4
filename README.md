# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

Proyecto desarrollado en Python para la Fase 4 del curso **Programación (213023)** de la UNAD, aplicando programación orientada a objetos y manejo avanzado de excepciones sin utilizar bases de datos.

## Descripción del proyecto
El sistema gestiona clientes, servicios y reservas en memoria mediante objetos y listas de Python, registrando los eventos y errores relevantes en un archivo de texto (`eventos_software_fj.log`) y manteniendo la ejecución estable ante datos inválidos o fallos en las operaciones.

## Servicios que maneja Software FJ
* **Reserva de salas (`ReservaSala`):** gestión de salas según capacidad y horas de reserva, con validación de rango de horas y cálculo de costo.
* **Alquiler de equipos (`AlquilerEquipo`):** alquiler de equipos según tipo y días de uso, validando la duración y calculando el valor correspondiente.
* **Asesorías especializadas (`AsesoriaEspecializada`):** asesorías según área o tema y horas contratadas, con validación de horas y cálculo de costo.

## Estructura del repositorio
* `excepciones.py`: excepciones personalizadas del sistema.
* `logger.py`: registro de eventos y errores en archivo de log.
* `entidad.py`: clase abstracta base para entidades del sistema.
* `cliente.py`: clase `Cliente` con encapsulación y validaciones.
* `servicios.py`: clase abstracta `Servicio` y servicios especializados con variantes de cálculo de costo.
* `reserva.py`: clase `Reserva` con confirmación, cancelación, procesamiento, bloques `try/except/else/finally` y encadenamiento de excepciones.
* `main.py`: simulación secuencial de 12 operaciones (válidas e inválidas, exitosas y fallidas).

## Cómo ejecutar `main.py`
1. Descarga o clona el repositorio en tu equipo.
2. Abre una terminal o consola dentro de la carpeta del proyecto.
3. Ejecuta el archivo principal con Python:

```bash
python main.py
