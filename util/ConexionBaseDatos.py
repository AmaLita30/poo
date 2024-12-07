import mysql.connector

class ConexionBaseDatos:

    def __init__(self) -> None:
        self.conexion =  mysql.conncetor.connext(host='localhost', database='dbnotas',user='root',password='123456')

    def getConexion(self):
        return self.conexion    
