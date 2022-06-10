import pymysql

try:                                    #Se crea la conexión a la base de datos local dentro de un try para confirmar la conexión.
  conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'aquelarre'
    db = 'biblioteca'
  )
  print("\n-- Conexion correcta.")      
 except:
  print("\n-- Fallo en la conexión.")

cursor = conexion.cursor()              #Se crea un cursor para manejar las entradas y salidas de la base de datos.

sql = "SELECT * FROM libros;"           #Se crea una variable que contenga el query a ejecutar en la base de datos.

#Ahora se intenta ejecutar el query dentro de un try para capturar errores en caso de que los haya.

try:
    cursor.execute(sql)
    print("\n-- Query ejecutado correctamente.\n")
    result = cursor.fetchall()
    for row in result:
        print(row)
except:
    print("\n-- Fallo en el query.")

conexion.commit()             #Por ultimo se guardan los cambios en la base.
