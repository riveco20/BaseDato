import psycopg2

''' sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
           #llavesPrimarias=((1,2,3),)
           llavesPrimarias=(tuple(input('Propociona las id\'s a buscar(separados por comas): ').split(',')),)#tupla de tupla
           cursor.execute(sentencia,llavesPrimarias)
           registro= cursor.fetchall()
           for registros in registro:
               print(registros)'''  # busar o mostrar informacion
'''
sentencia='INSERT INTO persona(nombre,apellido,email) VALU
valores=(('jesu','moren','jesumoren@gmail.com'),          
         ('marcos','lara','marcolara@gmail.com'),         
         ('maria','gonazales','mgonzales@gmail.com')      
         )                                                
cursor.executemany(sentencia,valores)                     
#conexion.commit()                                        
registrosInsertados=cursor.rowcount                       
print(f'Registros insertados: {registrosInsertados}')'''#Insertar varios registros
'''sentencia = 'UPDATE persona SET nombre=%s,apellido=%s, email=%s WHERE id_persona=%s'
valores = (('juan', 'perez', 'jperez@gmail.com', 1),
           ('sandy', 'salas', 'sandysalas@gmail.com', 2))
cursor.executemany(sentencia, valores)
registrosActualizados = cursor.rowcount
print(f'Registros Actualizado: {registrosActualizados}')'''#Actualizar varios registros
'''
sentencia='DELETE FROM persona WHERE id_persona=%s'
            entrada=input('Proporcione el valor del id_persona a eliminar: ')
            valores=(entrada,)
            cursor.execute(sentencia,valores)
            registrosEliminados=cursor.rowcount
            print(f'Registros Eliminados: {registrosEliminados}')'''#Eliminar un solo registro
'''sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
entrada = input('Proporcione el valor del id_persona a eliminar (separados por comas ').split(',')
valores = ((tuple(entrada, )),)
cursor.execute(sentencia, valores)
registrosEliminados = cursor.rowcount
print(f'Registros Eliminados: {registrosEliminados}')
'''#Eliminar varios Registros
conexion=psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia='DELETE FROM persona WHERE id_persona IN %s'
            entrada=input('Proporcione el valor del id_persona a eliminar (separados por comas ').split(',')
            valores=((tuple(entrada,)),)
            cursor.execute(sentencia,valores)
            registrosEliminados=cursor.rowcount
            print(f'Registros Eliminados: {registrosEliminados}')
except Exception as e:
   print(f'Ocurrio un error {e}')
finally:
    conexion.close()