# blog/operaciones.py
# Operaciones del blog: listar, buscar y filtrar posts.
# Todas las funciones reciben la lista de posts por parámetro.


def obtener_nombre_autor(post):
    """Retorna el nombre del autor sin romperse si falta algún dato."""
    autor = post.get("autor")
    if isinstance(autor, dict):
        return autor.get("nombre", "Autor desconocido")
    return "Autor desconocido"


def mostrar_posts(lista):
    """Imprime título, autor y estado de cada post de la lista."""
    for post in lista:
        # .get() evita un KeyError si falta alguna clave
        titulo = post.get("titulo") or "(sin título)"
        estado = post.get("estado", "sin estado")
        autor = obtener_nombre_autor(post)
        print(f"- {titulo} | Autor: {autor} | Estado: {estado}")


def listar_posts(lista):
    """Muestra todos los posts de la lista."""
    if not lista:
        print("No hay posts cargados.")
        return
    print("\nPosts disponibles:")
    mostrar_posts(lista)


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo título contiene el término."""
    resultados = []
    for post in lista:
        titulo = post.get("titulo", "")
        # .lower() en ambos lados para ignorar mayúsculas/minúsculas
        if isinstance(titulo, str) and termino.lower() in titulo.lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tienen el tag indicado."""
    resultados = []
    for post in lista:
        tags = post.get("tags", [])
        # Si tags no es una lista, el post se saltea para no romper el programa
        if not isinstance(tags, list):
            continue
        for etiqueta in tags:
            if str(etiqueta).lower() == tag.lower():
                resultados.append(post)
                break  # evita agregar el mismo post dos veces
    return resultados
