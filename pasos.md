# Pasos creación librerías Python

## Idea y planificación
[x] Definir claramente el propósito de la librería y qué problemas resolverá.
[x] Investigar si existen librerías similares y analiza qué las diferencia de tu idea.
[x] Diseñar una estructura básica de la librería y las principales funciones o clases que necesitarás.
[x] Eligir un nombre y crea un repositorio

## Escoger un nombre descriptivo y único para tu librería.
[x] Crer un repositorio en una plataforma de alojamiento de código como GitHub, GitLab o Bitbucket.
[x] Configura el entorno de desarrollo:

## Crear entorno.
[x] Configura un entorno virtual para el desarrollo. Puedes usar venv o virtualenv para ello.

## Definir una estructura de carpetas para tu proyecto. Ejemplo

mi_libreria/
    ├── mi_libreria/
    │   ├── __init__.py
    │   ├── modulo1.py
    │   ├── modulo2.py
    │   └── ...
    ├── tests/
    │   ├── test_modulo1.py
    │   ├── test_modulo2.py
    │   └── ...
    ├── setup.py
    └── README.md

## Codificación
[] Seguir las mejores prácticas de programación de Python
[] Documentar bien el código con docstrings.

## Pruebas unitarias
[] Crear pruebas unitarias para asegurarte de que el código funcione correctamente.
[] Utilizar bibliotecas como unittest o pytest para escribir y ejecutar pruebas.

## Documentación
[] Crear una documentación clara y completa para tu librería. Puedes usar herramientas como Sphinx para generar documentación a partir de los docstrings.
[] Añadir ejemplos

## Empaquetado
[] Prepara tu librería para su distribución mediante empaquetado.
[] Crear un archivo setup.py para definir los detalles de la distribución.

## Distribución
[] Publicar la librería en el Python Package Index (PyPI).

Recurso para usar Github actions [https://medium.com/@VersuS_/automate-pypi-releases-with-github-actions-4c5a9cfe947d](https://medium.com/@VersuS_/automate-pypi-releases-with-github-actions-4c5a9cfe947d)

https://www.youtube.com/watch?v=3i797U2C-Bk
https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Versionado
[] Utilizar un sistema de control de versiones (Git) y seguir las convenciones de versionado semántico para gestionar las versiones de la librería.

## Licencia
[] Decidir qué tipo de licencia asignar a la librería.

## Colaboración y mantenimiento:
[] Invitar a otr@s desarrollador@s a colaborar en el proyecto.
[] Escuchar los comentarios de la comunidad y mantener la librería actualizada.