from contacto import Contacto

class Servicio_Contacto:

    ARCHIVO = 'contactos.txt'
    
    def __init__(self):
        self.contactos = []
        # Obtener contactos en la lista
        self.contactos = self.obtener_contactos()

    def obtener_contactos(self):
        """ Función para obtener los contactos del documento, si no hay documento, lo crea """
        try:
            contactos = []
            with open(self.ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    nombre, telefono, email = linea.strip().split(',')
                    contacto = Contacto(nombre, telefono, email)
                    contactos.append(contacto)
        except FileNotFoundError:
            print('Archivo de contactos no encontrado. Se creará uno nuevo')
            with open(self.ARCHIVO, 'a') as archivo:
                pass
        except Exception as e:
            print(f'Ocurrió un error al obtener contactos: {e}')
        return contactos

    def guardar_contactos(self, contactos):
        """ Función para guardar un contacto en el documento """
        try:
            with open(self.ARCHIVO, 'w') as archivo:
                for contacto in contactos:
                    archivo.write(f'{contacto.nombre},{contacto.telefono},{contacto.email}\n')
        except Exception as e:
            print(f'Ocurrió un error guardando el contacto: {e}')

    def agregar_contacto(self, contacto):
        """ Funcion que agrega un contacto al documento """
        self.contactos = self.obtener_contactos()
        self.contactos.append(contacto)
        self.guardar_contactos(self.contactos)

    def buscar_contacto(self, nombre):
        """ Función que busca un contacto mediante un nombre """
        try:
            contactos = self.obtener_contactos()
            for contacto in contactos:
                if contacto.nombre.lower() == nombre.lower():
                    print(f'Contacto: {contacto}')
                    return contacto
                else:
                    print(f'No se pudo encontrar contacto: {nombre}')
        except Exception as e:
            print(f'Ocurrió un error buscando el contacto: {e}')

    def eliminar_contacto(self, nombre):
        try:
            resultado = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
            if resultado:
                for c in resultado:
                    self.contactos.remove(c)
                self.guardar_contactos(self.contactos)
                print(f'Contacto {c.nombre} eliminado correctamente')
            else:
                print(f'No se pudo eliminar contacto: {nombre}')
        except Exception as e:
            print(f'Ocurrió un error al eliminar contacto: {e}')

    def mostrar_contactos(self):
        """ Muestra todos los contactos """
        try:
            print('Contactos en la Agenda:')
            contactos = self.obtener_contactos()
            for contacto in contactos:
                print(contacto)
        except Exception as e:
            print(f'Error al mostrar contactos: {e}')