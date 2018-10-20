'''
Created on 19 oct. 2018

@author: constanza
'''

# Creacion de la clase seguridad
class Seguridad:
    # Diccionario de la clase Seguridad para guardar los correos con sus claves válidas
    diccionario = {}

    # Metodos de la clase seguridad

    def registrarUsuario(self, correo, clave1, clave2):
        self.diccionario[correo] = clave1[::-1]
        return 'Usuario aceptado'
    
    def ingresarUsuario(self, correo, clave):
        if correo in self.diccionario and self.diccionario.get(correo,"none")[::-1] == clave:
            return 'Usuario aceptado'
