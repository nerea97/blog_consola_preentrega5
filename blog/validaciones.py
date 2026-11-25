# blog/validaciones.py
# Reglas lógicas del sistema: validación de la estructura de los posts.

from blog.datos import estados_post

# Claves que todo post debe tener
CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Retorna (True, "válido") o (False, mensaje con los errores)."""
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    errores = []

    # 1. Claves obligatorias: se verifican con "in" antes de usarlas
    for clave in CLAVES_OBLIGATORIAS:
        if clave not in post:
            errores.append(f'falta la clave "{clave}"')

    # 2. Título y contenido no vacíos
    for campo in ("titulo", "contenido"):
        if campo in post:
            valor = post[campo]
            if not isinstance(valor, str) or valor.strip() == "":
                errores.append(f'"{campo}" está vacío')

    # 3. El autor debe ser un diccionario con la clave "nombre"
    if "autor" in post:
        autor = post["autor"]
        if not isinstance(autor, dict):
            errores.append('"autor" no es un diccionario')
        elif "nombre" not in autor:
            errores.append('el autor no tiene la clave "nombre"')

    # 4. Los tags deben ser una lista
    if "tags" in post and not isinstance(post["tags"], list):
        errores.append('"tags" no es una lista')

    # 5. El estado debe pertenecer a la tupla estados_post
    if "estado" in post and post["estado"] not in estados_post:
        errores.append(f'estado "{post["estado"]}" no es válido')

    if errores:
        return False, "; ".join(errores)
    return True, "válido"
