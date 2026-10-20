from datetime import date

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, correo, contrasena, rol):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena
        self._rol = rol

    @property
    def id_usuario(self): return self._id_usuario
    @property
    def nombre(self): return self._nombre
    @property
    def correo(self): return self._correo
    @property
    def rol(self): return self._rol

    def crear_proyecto(self, nombre, descripcion):
        return Proyecto(None, nombre, descripcion, date.today(), self._id_usuario)

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self._rol})"


class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_creacion, id_lider):
        self._id_proyecto = id_proyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_creacion = fecha_creacion
        self._id_lider = id_lider
        self._miembros = []
        self._tableros = []

    def agregar_miembro(self, usuario):
        if usuario.id_usuario not in [m.id_usuario if hasattr(m,'id_usuario') else m for m in self._miembros]:
            self._miembros.append(usuario)
            return True
        return False

    def crear_tablero(self, nombre):
        nuevo_tablero = Tablero(None, nombre, self._id_proyecto)
        self._tableros.append(nuevo_tablero)
        return nuevo_tablero

    @property
    def nombre(self): return self._nombre
    @property
    def miembros(self): return self._miembros
    @property
    def tableros(self): return self._tableros


class Tablero:
    def __init__(self, id_tablero, nombre, id_proyecto):
        self._id_tablero = id_tablero
        self._nombre = nombre
        self._id_proyecto = id_proyecto
        self._columnas = []

    def agregar_columna(self, nombre, orden):
        nueva_columna = Columna(None, nombre, orden, self._id_tablero)
        self._columnas.append(nueva_columna)
        self._columnas.sort(key=lambda c: c._orden)
        return nueva_columna

    @property
    def nombre(self): return self._nombre
    @property
    def columnas(self): return self._columnas


class Columna:
    def __init__(self, id_columna, nombre, orden, id_tablero):
        self._id_columna = id_columna
        self._nombre = nombre
        self._orden = orden
        self._id_tablero = id_tablero
        self._tareas = []

    def agregar_tarea(self, tarea):
        self._tareas.append(tarea)

    @property
    def nombre(self): return self._nombre
    @property
    def tareas(self): return self._tareas


class Tarea:
    def __init__(self, id_tarea, titulo, descripcion, fecha_creacion,
                 fecha_limite=None, estado="Pendiente", id_responsable=None):
        self._id_tarea = id_tarea
        self._titulo = titulo
        self._descripcion = descripcion
        self._fecha_creacion = fecha_creacion
        self._fecha_limite = fecha_limite
        self._estado = estado
        self._id_responsable = id_responsable

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def asignar_responsable(self, id_usuario):
        self._id_responsable = id_usuario

    @property
    def titulo(self): return self._titulo
    @property
    def estado(self): return self._estado


if __name__ == "__main__":
    print("=== PRUEBA DEL SISTEMA DE GESTIÓN DE PROYECTOS ===")
    oscar = Usuario(1, "Oscar", "Carrillo", "oscar@correo.cl", "123456", "líder")
    print(f"Usuario creado: {oscar}")
    proyecto = oscar.crear_proyecto("Sistema Trello", "Plataforma de gestión de tareas")
    print(f"Proyecto creado: {proyecto.nombre}")
    tablero = proyecto.crear_tablero("Tablero Principal")
    col1 = tablero.agregar_columna("Pendiente", 1)
    col2 = tablero.agregar_columna("En Progreso", 2)
    col3 = tablero.agregar_columna("Terminado", 3)
    tarea1 = Tarea(1, "Diseñar UML", "Hacer diagrama de clases", date.today())
    col1.agregar_tarea(tarea1)
    print(f"\nColumnas: {[c.nombre for c in tablero.columnas]}")
    print(f"Tareas en Pendiente: {[t.titulo for t in col1.tareas]}")
    print("\n✅ Sistema funcionando")