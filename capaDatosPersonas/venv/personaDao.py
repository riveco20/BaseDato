from conexion import Conexion
from persona import Persona
from logger_base import log
class PErsonaDAO:
    '''
    DAO( Data Aceess Object)
    CRUD(Create-Read_Update-Delete)
    '''
    _SELECCIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR ='INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido =%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def selecionar(cls):
        with Conexion.obtenerConexion():
           with Conexion.obtenerCursor() as cursor:
                 cursor.execute(cls._SELECCIONAR)
                 registros=cursor.fetchall()
                 personas=[]
                 for registro in registros:
                     persona = Persona(registro[0],registro[1],registro[2],registro[3])
                     personas.append(persona)
                 return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                valores=(persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertar {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores=(persona.nombre,persona.apellido,persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Objeto eliminado {persona}')
                return cursor.rowcount

if __name__ == '__main__':
    #Insertar un registro
#    persona1=Persona(nombre='Carla',apellido='Vegas',email='cvegas@mail.com')
 #   personas_insertadas= PErsonaDAO.insertar(persona1)
  #  log.debug(f'Personas insertadas {personas_insertadas} ')

    # Actualizar un registro
    #persona1 = Persona(2, 'Nicole', 'Peña', 'nicolPeña@email.com')
    #perosona_actualizadas = PErsonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas: {perosona_actualizadas}')

    #Eliminaar un Registro
    persona1=Persona(id_persona=14)
    persona_eliminadas = PErsonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {persona_eliminadas}')

    #seleccionar objetos
    personas=PErsonaDAO.selecionar()
    for persona in personas:
        log.debug(persona)