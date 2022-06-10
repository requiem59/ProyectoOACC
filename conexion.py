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

sql = "SELECT * FROM libros;"

try:
    cursor.execute(sql)
    print("\n-- Query ejecutado correctamente.\n")
    result = cursor.fetchall()
    for row in result:
        print(row)
except:
    print("\n-- Fallo en el query.")

conexion.commit()
