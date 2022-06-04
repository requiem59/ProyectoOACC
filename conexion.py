import pymysql

conexion = pymysql.connect(
  host = 'localhost',
  user = 'root',
  password = 'aquelarre'
  db = 'biblioteca'
)

cursor = conexion.cursor()
