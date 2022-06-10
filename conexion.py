"""
Conexión hacía un servicio SQL en localhost
Creado por:
  Mejia Mondragón Cristian Alexis
  Pacheco Ramírez Shai Karel
  
"""
#Setup de la conexión a local
import pymysql

conexion = pymysql.connect(
  host = 'localhost',
  user = 'root',
  password = 'aquelarre'
  db = 'biblioteca'
)

cursor = conexion.cursor()

#Formato de los creates
SQL = "INSERT INTO users(nombre, apellido, correo) VALUES('karel', 'pacheco', 'karelpacheco36@aragon.unam.mx')"
cursor.execute(sql)
SQL = "INSERT INTO users(nombre, apellido, correo) VALUES('cristian', 'mejia', 'christianmejia@aragon.unam.mx')"
cursor.execute(sql)


#Formato del update
SQL = "UPDATE SET correo = 'christianmejia10@aragon.unam.mx' WHERE (nombre ='cristian' AND apellido = 'mejia')
cursor.execute(sql)


#Formato de los delete
SQL = "DELETE FROM users WHERE (nombre ='cristian' AND apellido = 'mejia')
cursor.execute(sql)


connection.commit()
