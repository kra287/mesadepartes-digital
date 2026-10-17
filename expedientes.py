"""Módulo de expedientes: generar número, guardar, buscar y ordenar."""

from datetime import date

ARCHIVO = "expedientes.txt"
SEPARADOR = "|"


def generar_expediente(cantidad_actual):
    """Crea un número de expediente único: EXP-2026-0001, EXP-2026-0002, ..."""
    anio = date.today().year
    return "EXP-" + str(anio) + "-" + str(cantidad_actual + 1).zfill(4)


def guardar_expediente(registro):
    """Guarda un registro (lista de datos) en el archivo, una línea por trámite."""
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(SEPARADOR.join(registro) + "\n")


def cargar_expedientes():
    """Lee el archivo y devuelve una lista de registros. Si no existe, lista vacía."""
    registros = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    registros.append(linea.split(SEPARADOR))
    except FileNotFoundError:
        pass
    return registros


def buscar_expediente(registros, numero):
    """Busca por número de expediente. Devuelve el registro o None."""
    for registro in registros:
        if registro[0] == numero.strip().upper():
            return registro
    return None


def ordenar_por_fecha(registros):
    """Ordena los registros por fecha (la fecha se guarda como AAAA-MM-DD)."""
    return sorted(registros, key=lambda r: r[1])
