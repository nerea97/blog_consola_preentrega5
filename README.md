# Blog de consola en Python

Sistema de blog por consola desarrollado para la Diplomatura en Inteligencia
Artificial - Python (Coderhouse), Preentrega 5.

El programa guarda los posts en memoria y permite consultarlos desde un menú
interactivo. Esta versión está organizada en módulos y paquetes: cada archivo
tiene una responsabilidad concreta.

**Autora:** Nerea Onieva

## Cómo ejecutarlo

Requisito: tener Python 3 instalado. No usa librerías externas.

1. Abrí una terminal en la carpeta raíz del proyecto (donde está `main.py`).
2. Ejecutá:

```bash
python main.py
```

> Si aparece un error de importación, revisá que estés parado en la carpeta
> donde está `main.py` y no dentro de `blog/`.

## Funcionalidades del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

| Opción | Qué hace |
|---|---|
| 1. Ver todos los posts | Muestra título, autor y estado de cada post. |
| 2. Buscar por titulo | Pide un término y muestra los posts cuyo título lo contiene. No distingue mayúsculas de minúsculas. |
| 3. Filtrar por tag | Pide un tag y muestra los posts que lo tienen. No distingue mayúsculas de minúsculas. |
| 4. Validar posts | Revisa la estructura de cada post e indica si es válido o qué errores tiene. |
| 5. Salir | Muestra un mensaje de despedida y termina el programa. |

El programa no se cierra si el usuario escribe texto en el menú, elige una
opción inexistente o deja vacía una búsqueda: muestra un aviso y vuelve al menú.

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Archivo que se ejecuta. Importa las piezas del paquete `blog` y coordina el menú dentro de `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog/` como paquete. |
| `blog/datos.py` | Datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. |
| `blog/menu.py` | Interacción con el usuario: `mostrar_menu()` (con `try-except`) y `pedir_texto()`. |
| `blog/operaciones.py` | `listar_posts(lista)`, `buscar_por_titulo(lista, termino)` y `filtrar_por_tag(lista, tag)`. |
| `blog/validaciones.py` | `validar_post(post)`: claves obligatorias, campos no vacíos, autor como diccionario, tags como lista y estado válido. |

Los imports van en una sola dirección para evitar imports circulares:
`main.py` importa de los módulos del paquete, y `validaciones.py` importa
`estados_post` desde `datos.py`. `datos.py` no importa nada.

## Datos de prueba

`blog/datos.py` incluye 5 posts. Los 3 primeros son válidos y los posts 4 y 5
tienen errores a propósito para probar la opción **4. Validar posts**:

- Post 4: le falta la clave `contenido` y el título está vacío.
- Post 5: `tags` es un texto en lugar de una lista y el estado `pendiente`
  no existe en `estados_post`.


## Cumplimiento de la consigna

| Requisito | Dónde se cumple |
|---|---|
| Carpeta raíz del proyecto con `main.py` | `main.py` en la raíz del repositorio |
| Paquete `blog/` con `__init__.py` | `blog/__init__.py` |
| Datos base separados | `blog/datos.py`: `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts` |
| Autor como diccionario anidado | En `blog/datos.py` cada post usa `"autor": perfil_autor` |
| Menú e `input()` separados | `blog/menu.py`: `mostrar_menu()` (con `try-except`) y `pedir_texto()` |
| Búsqueda y filtrado separados | `blog/operaciones.py`: `listar_posts(lista)`, `buscar_por_titulo(lista, termino)` y `filtrar_por_tag(lista, tag)` |
| `.lower()` en búsquedas y filtros | `buscar_por_titulo()` y `filtrar_por_tag()` en `blog/operaciones.py` |
| Validaciones separadas | `blog/validaciones.py`: `validar_post(post)` |
| Imports con `from blog.modulo import funcion` | Primeras líneas de `main.py` |
| Ejecución protegida | `main.py` termina con `if __name__ == "__main__":` |
| Sin imports circulares | `datos.py`, `menu.py` y `operaciones.py` no importan otros módulos del paquete; `validaciones.py` solo importa `estados_post` de `datos.py` |
| Opción 1 muestra título, autor y estado | Ver el ejemplo de ejecución |

## Ejemplo de ejecución

Salida real de `python main.py` probando las opciones 1, 2 (`python`), 3 (`ia`),
un texto inválido en el menú (`hola`), la opción 4 y la salida. Se omiten las
líneas del menú que se repiten.

```
$ python main.py
Elegí una opción: 1

Posts disponibles:
- Primeros pasos con Python | Autor: Nerea Onieva | Estado: publicado
- Cómo la IA puede optimizar procesos logísticos | Autor: Nerea Onieva | Estado: borrador
- Organizando datos con diccionarios | Autor: Nerea Onieva | Estado: archivado
- (sin título) | Autor: Nerea Onieva | Estado: publicado
- Módulos y paquetes en Python | Autor: Nerea Onieva | Estado: pendiente

Elegí una opción: 2
Buscar por titulo: python

Posts que contienen "python":
- Primeros pasos con Python | Autor: Nerea Onieva | Estado: publicado
- Módulos y paquetes en Python | Autor: Nerea Onieva | Estado: pendiente

Elegí una opción: 3
Ingresá un tag: ia

Posts con el tag ia:
- Cómo la IA puede optimizar procesos logísticos | Autor: Nerea Onieva | Estado: borrador

Elegí una opción: hola
Error: tenés que ingresar un número del 1 al 5.

Elegí una opción: 4

Validación de posts:
Post 1: válido
Post 2: válido
Post 3: válido
Post 4: error - falta la clave "contenido"; "titulo" está vacío
Post 5: error - "tags" no es una lista; estado "pendiente" no es válido

Elegí una opción: 5
Gracias por usar el sistema del blog. ¡Hasta luego!
```
