import psycopg2

conexion=psycopg2.connect(user='postgres',password='ciwawa37',host='127.0.0.1',port='5432',database='test_db')

try:
        with conexion :
            with conexion.cursor() as cursor:
                sentencia ='INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
                valores=('muichel','rojas','mrojas@gmail.com')
                cursor.execute(sentencia, valores)

                sentecia='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
                valores=('juanes','acosta','juanacosta@gmail.com',1)
                cursor.execute(sentencia, valores)
                #conexion.commit()

except Exception as e:

   print(f'Ocurrio un error {e}')
finally:
    conexion.close()
    print('Termian la transacion')