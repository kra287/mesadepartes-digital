"""Mesa de Partes Digital - prototipo en Python.
Curso: Fundamentos de Programación (CIIN1205P) - UPN
"""

from datetime import date

from validacion import validar_registro
from expedientes import (
    generar_expediente,
    guardar_expediente,
    cargar_expedientes,
    buscar_expediente,
    ordenar_por_fecha,
)


def mostrar_expediente(registro):
    """Imprime los datos de un expediente."""
    numero, fecha, dni, nombres, tipo, asunto, folios = registro
    print("Expediente:", numero)
    print("Fecha:", fecha)
    print("DNI:", dni)
    print("Nombres:", nombres)
    print("Tipo de documento:", tipo)
    print("Asunto:", asunto)
    print("Folios:", folios)


def registrar():
    """Pide los datos, los valida y guarda el trámite."""
    valido = False
    while not valido:
        dni = input("Ingrese DNI: ").strip()
        nombres = input("Ingrese nombres: ").strip()
        tipo = input("Ingrese tipo de documento: ").strip()
        asunto = input("Ingrese asunto: ").strip()
        folios = input("Ingrese cantidad de folios: ").strip()

        valido, mensaje = validar_registro(dni, nombres, tipo, asunto, folios)
        if not valido:
            print("Datos inválidos:", mensaje)

    registros = cargar_expedientes()
    numero = generar_expediente(len(registros))
    fecha = date.today().isoformat()  # AAAA-MM-DD
    guardar_expediente([numero, fecha, dni, nombres, tipo, asunto, folios])

    print("Registro exitoso")
    print("Cargo de recepción - N.º de expediente:", numero)


def consultar():
    """Busca un expediente por su número."""
    numero = input("Ingrese número de expediente: ")
    registro = buscar_expediente(cargar_expedientes(), numero)
    if registro is not None:
        mostrar_expediente(registro)
    else:
        print("Expediente no encontrado")


def listar():
    """Muestra todos los expedientes ordenados por fecha."""
    registros = ordenar_por_fecha(cargar_expedientes())
    if len(registros) == 0:
        print("Aún no hay expedientes registrados.")
    for registro in registros:
        print("-" * 30)
        mostrar_expediente(registro)


def main():
    opcion = ""
    while opcion != "4":
        print("\n=== MESA DE PARTES DIGITAL ===")
        print("1. Registrar trámite")
        print("2. Consultar expediente")
        print("3. Listar expedientes por fecha")
        print("4. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            registrar()
        elif opcion == "2":
            consultar()
        elif opcion == "3":
            listar()
        elif opcion == "4":
            print("Hasta pronto.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
