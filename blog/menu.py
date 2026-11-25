# blog/menu.py
# Interacción con el usuario: menú y lectura de datos con input().


def mostrar_menu():
    """Muestra el menú y retorna la opción elegida (o None si es texto)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        # int() falla si el usuario escribe texto: lo captura el except
        return int(input("Elegí una opción: "))
    except ValueError:
        print("Error: tenés que ingresar un número del 1 al 5.")
        return None


def pedir_texto(mensaje):
    """Pide un texto y retorna None si el usuario lo deja vacío."""
    texto = input(mensaje).strip()
    if texto == "":
        print("Error: no ingresaste ningún texto.")
        return None
    return texto
