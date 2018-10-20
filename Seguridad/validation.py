'''
Created on 19 oct. 2018

@author: constanza
'''
# Importamos el modulo re para Expresiones Regulares (Regular expressions)
# Este modulo sera utilizado para comprobar que la clave ingresada por el usuario
# al registrarse sea una clave alfanumerica
import re

# Importamos el metodo validate_email que contiene las expresiones regulares para saber
# si un correo cumple con la especificación del RFC 822
from validar_email import validate_email

# Creacion de la clase seguridad
class Seguridad:
    # Diccionario de la clase Seguridad para guardar los correos con sus claves válidas
    diccionario = {}

    # Metodos de la clase seguridad

    def registrarUsuario(self, correo, clave1, clave2):
        
        # Verificar que ya no exista un usuario con el mismo correo
        if correo in self.diccionario:
            return "Correo electronico invalido"
        
        if (correo == "" or clave1=="" or clave2==""):
            return "Debe llenar campos"
        
        # Verificamos que el correo electronico ingresado tenga el formato especificado por el RFC 822
        # utilizando el método validate_email
        if validate_email(correo):
            pass

        # Si el correo no es valido, retornamos un mensaje de error
        else:
            return "Correo electronico invalido"
        
        # Verificamos que las dos claves coinciden, que la longitud es entre 8 y 16, que 
        # sea alfanumerica, que contenga al menos un digito, una mayuscula y una minuscula
        if clave1 == clave2 and len(clave1) >= 8 and len(clave1) <= 16 and re.search(r"\w", clave1) \
        and re.search(r"\d", clave1) and re.search(r"[A-Z]", clave1) and re.search(r"[a-z]", clave1):

            # Ahora verificamos que la clave contenga al menos 3 letras
            cantidadLetras = 0
            for letra in clave1:
                if re.match(r"[A-Za-z]", clave1):
                    cantidadLetras += 1

            # Si la cantidad de letras es menor a 3, entonces la clave es invalida
            if cantidadLetras < 3:
                return "Clave invalida"
            # Si la cantidad de letras es mayor a 3, entonces
            # guardamos el correo con la clave codificada en el diccionario de la clase seguridad
            # La codificacion es el mismo string de la clave en reversa
        
            self.diccionario[correo] = clave1[::-1]
            return 'Usuario aceptado'
        # Si las claves no coinciden, entonces la clave es invalida
        else:
            return "Clave invalida"

        
        
    def ingresarUsuario(self, correo, clave):
        # Comprobamos que el correo se encuentre en el diccionario
        
        if (correo == "" or clave==""):
            return "Debe llenar campos"

        # Si el correo esta en el diccionario y la clave coincide con la guardada, entonces
        # el usuario es aceptado en el sistema
        if correo in self.diccionario and self.diccionario.get(correo,"none")[::-1] == clave:
            return 'Usuario aceptado'
 

        # Si el usuario esta en el diccionario pero la clave no coincide con la guardada,
        # entonces emitimos un mensaje de clave invalida
        elif correo in self.diccionario and self.diccionario.get(correo,"none")[::-1] != clave:
            return 'Clave invalida'
            

        # Si el correo no esta en el diccionario, el usuario es invalido
        return 'Usuario invalido'

