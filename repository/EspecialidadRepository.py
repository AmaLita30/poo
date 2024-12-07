from util.ConexionBaseDatos import ConexionBaseDatos

class EspecialidadRepository:

    def __init__(self) -> None:
        self.conexion = ConexionBaseDatos.getConexion()

    def listarEspecialidades(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM especialidad"
        cursor.execute(sql)
        return cursor.fetchall()