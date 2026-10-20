import mysql.connector
from mysql.connector import Error

class ConexionDB:
    def __init__(self):
        self._host = "localhost"
        self._usuario = "root"
        self._contrasena = ""  # WampServer no tiene contraseña por defecto
        self._base_datos = "gestion_proyectos"
        self._conexion = None

    def conectar(self):
        try:
            self._conexion = mysql.connector.connect(
                host=self._host,
                user=self._usuario,
                password=self._contrasena,
                database=self._base_datos
            )
            if self._conexion.is_connected():
                print("✅ Conexión exitosa a la base de datos")
                return self._conexion
        except Error as e:
            print(f"❌ Error de conexión: {e}")
            return None

    def cerrar(self):
        if self._conexion and self._conexion.is_connected():
            self._conexion.close()
            print("🔌 Conexión cerrada")


if __name__ == "__main__":
    db = ConexionDB()
    db.conectar()
    db.cerrar()