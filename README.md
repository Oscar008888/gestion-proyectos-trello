# Sistema de Gestión de Proyectos tipo Trello

Asignatura: Programación Orientada a Objeto Seguro - INACAP
Grupo: 3
Integrante: Oscar Carrillo

## Descripción
Sistema para gestionar proyectos mediante tableros, columnas y tareas. Desarrollado en Python con programación orientada a objetos y conexión a base de datos MySQL.

## Estructura
- `modelos.py` → Clases: Usuario, Proyecto, Tablero, Columna, Tarea
- `conexion_db.py` → Conexión a base de datos
- `base_datos.sql` → Creación de tablas y datos de prueba

## Requisitos
- Python 3.x
- WampServer (MySQL)
- Conector: `pip install mysql-connector-python`

## Ejecución
1. Ejecutar `base_datos.sql` en phpMyAdmin
2. Ejecutar: `python modelos.py`
3. Probar conexión: `python conexion_db.py`