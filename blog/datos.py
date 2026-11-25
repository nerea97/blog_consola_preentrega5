# blog/datos.py
# Datos base del blog: autor, estados, etiquetas y posts en memoria.

# Perfil del autor: diccionario con una lista anidada de redes sociales
perfil_autor = {
    "nombre": "Nerea Onieva",
    "bio": "Estudiante de IA y entusiasta de la automatización.",
    "especialidad": "Python e IA aplicada a procesos",
    "redes_sociales": ["@nerea_dev", "@nerea_python"]
}

# Estados posibles de un post: tupla con valores fijos del sistema
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas del blog: set ("Python" se repite, el set lo guarda una vez)
etiquetas_blog = {"Python", "IA", "Automatización", "Web", "Backend", "Python"}

# Lista de posts: los 3 primeros son válidos, el 4 y el 5 tienen errores
# a propósito para probar las validaciones
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Cómo empezar a programar con Python desde cero.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[1]  # "publicado"
    },
    {
        "id": 2,
        "titulo": "Cómo la IA puede optimizar procesos logísticos",
        "contenido": "Ideas para aplicar IA en el picking y el despacho.",
        "autor": perfil_autor,
        "tags": ["IA", "Automatización", "Logística"],
        "estado": estados_post[0]  # "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Los diccionarios guardan datos con pares clave-valor.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": estados_post[2]  # "archivado"
    },
    {
        # Post incompleto: falta la clave "contenido" y el título está vacío
        "id": 4,
        "titulo": "",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "publicado"
    },
    {
        # Post incorrecto: tags es texto y el estado no existe en la tupla
        "id": 5,
        "titulo": "Módulos y paquetes en Python",
        "contenido": "Cómo dividir un proyecto en varios archivos.",
        "autor": perfil_autor,
        "tags": "Python",
        "estado": "pendiente"
    }
]
