
#Importación de librerías:

from proyecto import Proyecto
from Conexion import Conexion
from tkinter import messagebox as mb

class BDatos:
    SELECCIONAR = 'SELECT * FROM proyecto'
    INSERTAR = 'INSERT INTO proyecto(descripcion,tematica,academia,prioridad,fecha_inicio,fecha_fin) VALUES(%s, %s, %s,%s, %s, %s)'
    ACTUALIZAR = 'UPDATE proyecto SET descripcion=%s, tematica=%s, academia=%s,prioridad=%s, fecha_inicio=%s, fecha_fin=%s WHERE codigo=%s'
    ELIMINAR = 'DELETE FROM proyecto WHERE codigo=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            proyectos = []
            for registro in registros:
                proyecto = Proyecto(registro[0], registro[1],
                                  registro[2], registro[3],
                                  registro[4], registro[5],registro[6])
                proyectos.append(proyecto)
            return proyectos
        except Exception as e:
            mb.showerror('Error', message='Ocurrio un error al seleccionar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, proyecto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (proyecto.descripcion, proyecto.tematica,proyecto.academia,proyecto.prioridad,proyecto.fecha_inicio,proyecto.fecha_fin)
            print('Crear', valores)  
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar proyecto: {e}')
            #mb.showerror('Error', message='Ocurrio un error al insertar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, proyecto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (proyecto.descripcion, proyecto.tematica,proyecto.academia,proyecto.prioridad,proyecto.fecha_inicio,proyecto.fecha_fin,proyecto.codigo)
            print('Modif', valores)         
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrio un error al Actuacizar proyecto: {e}')
            #mb.showerror('Error', message='Ocurrio un error al actualizar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, proyecto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (proyecto.codigo,)
            print('Delete', valores)  
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al borrar proyecto: {e}')
            #mb.showerror('Error', message='Ocurrio un error al borrar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':

    proyectos = BDatos.seleccionar()
    for proyecto in proyectos:
        print(proyecto)