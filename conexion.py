import pymysql

conexion = pymysql.connect(
  host = 'localhost',
  user = 'root',
  password = 'aquelarre'
  db = 'biblioteca'
)

cursor = conexion.cursor()

SQL = "INSERT INTO users(nombre, apellido, correo) VALUES('karel', 'pacheco', 'karelpacheco36@aragon.unam.mx')"
SQL = "INSERT INTO users(nombre, apellido, correo) VALUES('cristian', 'mejia', 'christianmejia10@aragon.unam.mx')"
cursor.execute(sql)

connection.commit()
