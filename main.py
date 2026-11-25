# main.py
# Archivo principal: importa las piezas del paquete "blog" y coordina el menú.

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import (
    listar_posts,
    buscar_por_titulo,
    filtrar_por_tag,
    mostrar_posts,
)
from blog.validaciones import validar_post


def opcion_buscar(lista):
    """Pide un término y muestra los posts encontrados."""
    termino = pedir_texto("Buscar por titulo: ")
    if termino is None:
        return
    encontrados = buscar_por_titulo(lista, termino)
    if encontrados:
        print(f'\nPosts que contienen "{termino}":')
        mostrar_posts(encontrados)
    else:
        print(f'No se encontraron posts con "{termino}".')


def opcion_filtrar(lista):
    """Pide un tag y muestra los posts que lo tienen."""
    tag = pedir_texto("Ingresá un tag: ")
    if tag is None:
        return
    encontrados = filtrar_por_tag(lista, tag)
    if encontrados:
        print(f"\nPosts con el tag {tag}:")
        mostrar_posts(encontrados)
    else:
        print(f'No hay posts con el tag "{tag}".')


def opcion_validar(lista):
    """Valida cada post y muestra si es válido o qué errores tiene."""
    print("\nValidación de posts:")
    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: error - {mensaje}")


def ejecutar():
    """Bucle principal: muestra el menú hasta que el usuario elija salir."""
    while True:
        opcion = mostrar_menu()

        # Si el usuario escribió texto, se vuelve a mostrar el menú
        if opcion is None:
            continue

        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            opcion_buscar(posts)
        elif opcion == 3:
            opcion_filtrar(posts)
        elif opcion == 4:
            opcion_validar(posts)
        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break
        else:
            # Número fuera del rango 1 a 5
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    ejecutar()
