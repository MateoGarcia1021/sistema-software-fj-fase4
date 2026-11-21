# main.py
# Simulacion de 12 operaciones completas sin base de datos.

from cliente import Cliente
from excepciones import DatoInvalidoError, OperacionReservaError
from logger import registrar_evento
from reserva import Reserva
from servicios import AlquilerEquipo, AsesoriaEspecializada, ReservaSala


def ejecutar_simulacion():
    clientes = []
    servicios = []
    reservas = []

    registrar_evento("INFO", "=== Inicio de simulacion Software FJ ===")

    # --- OPERACION 1: Registro valido de cliente ---
    try:
        c1 = Cliente("CL-01", "108800111", "Carlos Gomez", "carlos.gomez@correo.com")
        clientes.append(c1)
        print("Op 1 OK:", c1.resumen())
        registrar_evento("INFO", f"Op 1 OK: {c1.resumen()}")
    except DatoInvalidoError as err:
        print("Op 1 Error:", err)

    # --- OPERACION 2: Registro valido de segundo cliente ---
    try:
        c2 = Cliente("CL-02", "108800222", "Laura Perez", "laura.perez@correo.com")
        clientes.append(c2)
        print("Op 2 OK:", c2.resumen())
        registrar_evento("INFO", f"Op 2 OK: {c2.resumen()}")
    except DatoInvalidoError as err:
        print("Op 2 Error:", err)

    # --- OPERACION 3: Registro invalido de cliente (correo sin arroba) ---
    try:
        c3 = Cliente("CL-03", "108800333", "Pedro Ruiz", "pedro_correo_malo.com")
        clientes.append(c3)
    except DatoInvalidoError as err:
        print("Op 3 Error controlado:", err)
        registrar_evento("ERROR", f"Op 3 Error: {err}")

    # --- OPERACION 4: Registro invalido de cliente (nombre vacio) ---
    try:
        c4 = Cliente("CL-04", "108800444", "   ", "ana@correo.com")
        clientes.append(c4)
    except DatoInvalidoError as err:
        print("Op 4 Error controlado:", err)
        registrar_evento("ERROR", f"Op 4 Error: {err}")

    # --- OPERACION 5: Creacion valida de servicio ReservaSala ---
    try:
        s1 = ReservaSala("SV-01", "Sala Reuniones A", 50000, capacidad_personas=10, disponible=True)
        servicios.append(s1)
        print("Op 5 OK:", s1.describir())
        registrar_evento("INFO", f"Op 5 OK: {s1.describir()}")
    except DatoInvalidoError as err:
        print("Op 5 Error:", err)

    # --- OPERACION 6: Creacion valida de servicios AlquilerEquipo y AsesoriaEspecializada ---
    try:
        s2 = AlquilerEquipo("SV-02", "Portatil HP", 35000, tipo_equipo="Computo", disponible=True)
        s3 = AsesoriaEspecializada("SV-03", "Soporte Python", 80000, area_tema="Desarrollo", disponible=False)
        servicios.extend([s2, s3])
        print("Op 6 OK:", s2.describir(), "|", s3.describir())
        registrar_evento("INFO", "Op 6 OK: Servicios SV-02 y SV-03 creados.")
    except DatoInvalidoError as err:
        print("Op 6 Error:", err)

    # --- OPERACION 7: Creacion invalida de servicio (tarifa negativa) ---
    try:
        s_malo = AlquilerEquipo("SV-04", "Proyector", -10000, tipo_equipo="Video", disponible=True)
        servicios.append(s_malo)
    except DatoInvalidoError as err:
        print("Op 7 Error controlado:", err)
        registrar_evento("ERROR", f"Op 7 Error: {err}")

    # --- OPERACION 8: Creacion invalida de servicio (capacidad en cero) ---
    try:
        s_malo2 = ReservaSala("SV-05", "Sala Vacia", 40000, capacidad_personas=0, disponible=True)
        servicios.append(s_malo2)
    except DatoInvalidoError as err:
        print("Op 8 Error controlado:", err)
        registrar_evento("ERROR", f"Op 8 Error: {err}")

    # --- OPERACION 9: Reserva exitosa (Sala, 3 horas, descuento 10%) ---
    try:
        if clientes and servicios:
            r1 = Reserva("RS-01", clientes[0], servicios[0], cantidad=3)
            total1 = r1.procesar(descuento=0.10, impuesto=0.19)
            reservas.append(r1)
            print(f"Op 9 OK: Reserva {r1.codigo_reserva} confirmada. Total: ${total1}")
    except OperacionReservaError as err:
        print("Op 9 Error:", err, "| Causa:", err.__cause__)

    # --- OPERACION 10: Reserva exitosa (AlquilerEquipo, 2 dias, valores por defecto) ---
    try:
        if len(clientes) >= 2 and len(servicios) >= 2:
            r2 = Reserva("RS-02", clientes[1], servicios[1], cantidad=2)
            total2 = r2.procesar()
            reservas.append(r2)
            print(f"Op 10 OK: Reserva {r2.codigo_reserva} confirmada. Total: ${total2}")
    except OperacionReservaError as err:
        print("Op 10 Error:", err, "| Causa:", err.__cause__)

    # --- OPERACION 11: Reserva fallida por servicio no disponible (SV-03) ---
    try:
        if clientes and len(servicios) >= 3:
            r3 = Reserva("RS-03", clientes[0], servicios[2], cantidad=2)
            r3.procesar()
            reservas.append(r3)
    except OperacionReservaError as err:
        print("Op 11 Error controlado:", err, "| Causa:", err.__cause__)

    # --- OPERACION 12: Reserva fallida por horas fuera de rango (15 horas en sala) ---
    try:
        if len(clientes) >= 2 and servicios:
            r4 = Reserva("RS-04", clientes[1], servicios[0], cantidad=15)
            r4.procesar()
            reservas.append(r4)
    except OperacionReservaError as err:
        print("Op 12 Error controlado:", err, "| Causa:", err.__cause__)

    print("\n--- Resumen final en memoria ---")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas confirmadas: {len(reservas)}")
    registrar_evento("INFO", "=== Fin de simulacion Software FJ ===")


if __name__ == "__main__":
    ejecutar_simulacion()
