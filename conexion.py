import pymysql

try:
  conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'aquelarre'
    db = 'biblioteca'
  )
  print("\n-- Conexion correcta.")
 except:
  print("\n-- Fallo en la conexión.")

cursor = conexion.cursor()
