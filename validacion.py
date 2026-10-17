"""Módulo de validación: comprueba que los datos ingresados sean correctos."""


def validar_dni(dni):
    """El DNI debe tener exactamente 8 dígitos numéricos."""
    return len(dni) == 8 and dni.isdigit()


def validar_folios(texto):
    """Los folios deben ser un número entero mayor que 0."""
    return texto.isdigit() and int(texto) > 0


def validar_registro(dni, nombres, tipo_documento, asunto, folios):
    """Devuelve (True, "") si todo está bien, o (False, mensaje) si hay error."""
    if not validar_dni(dni):
        return False, "El DNI debe tener 8 dígitos."
    if len(nombres.strip()) == 0:
        return False, "Los nombres son obligatorios."
    if len(tipo_documento.strip()) == 0:
        return False, "El tipo de documento es obligatorio."
    if len(asunto.strip()) == 0:
        return False, "El asunto es obligatorio."
    if not validar_folios(folios):
        return False, "La cantidad de folios debe ser un número mayor que 0."
    return True, ""
