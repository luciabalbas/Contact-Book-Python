from servicio_contacto import Servicio_Contacto
from contacto import Contacto
import re

class Agenda_Contacto:
    def __init__(self):
        self.servicio_contacto = Servicio_Contacto()
        self.contactos = self.servicio_contacto.obtener_contactos()
        print('Agenda cargada correctamente') if self.contactos else print('No se pudo cargar agenda')

    def agenda_contacto(self):
        """ Aplicación de contactos """
        salir = False
        print('--- Agenda de Contactos ---')
        while not salir:
            try:
                opcion = self.menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrió un error: {e}')

    def menu(self):
        """ Muestra el menú de la aplicación, obtiene un valor int"""
        print(''' Menu
            1. Agregar Contacto
            2. Mostrar todos los Contactos
            3. Buscar Contacto
            4. Eliminar Contacto
            5. Salir''')
        return int(input('Introduzca opción: '))
        
    def ejecutar_opcion(self, opcion):
        """ Segun variable num, ejecuta una función """
        if opcion == 1:
            self.agregar_contacto()
        elif opcion == 2:
            self.servicio_contacto.mostrar_contactos()
        elif opcion == 3:
            self.buscar_contacto()
        elif opcion == 4:
            self.eliminar_contacto()
        elif opcion == 5:
            return True
        else:
            print('Opción no válida. Inténtelo de nuevo')
            return False
        
    def validar_correo(self, correo):
        """ Valida el correo mediante una expresion regular """
        regex_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(regex_email, correo)

    def agregar_contacto(self):
        """ Valida los inputs y en caso afirmativo, agrega un contacto al documento """
        try:
            nombre = input('Introduzca nombre: ')
            telefono = int(input('Introduca teléfono: '))
            email = input('Introduzca email: ')
            if not nombre or not telefono or not email:
                print('Los campos son obligatorios')
                raise ValueError
            if not self.validar_correo(email):
                print('Correo inválido')
                raise ValueError
        except Exception as e:
            print(f'Ocurrió un error al agregar contacto: {e}')
        else:
            nuevo_contacto = Contacto(nombre, telefono, email)
            self.servicio_contacto.agregar_contacto(nuevo_contacto)                

    def buscar_contacto(self):
        """ Mediante un input que recibe el nombre, busca un contacto """
        nombre = input('Introduzca nombre del contacto: ')
        self.servicio_contacto.buscar_contacto(nombre)

    def eliminar_contacto(self):
        """ Mediante un input que recibe un nombre, elimina un contacto"""
        nombre = input('Introduzca nombre del contacto: ')    
        self.servicio_contacto.eliminar_contacto(nombre)

# Aplicación del archivo
if __name__ == '__main__':
    agenda = Agenda_Contacto()
    agenda.agenda_contacto()
