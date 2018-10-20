'''
Created on 19 oct. 2018

@author: constanza
'''

from validation import *
import unittest

class testValidation(unittest.TestCase):
    
    def setUp(self):
        self.validacion = Seguridad()

# Pruebas interiores
    
    # Prueba para chequear que un usuario con datos validos se registra exitosamente
    def testRegistroUser(self):
        self.assertEqual(self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3bA1", "pru3bA1"), "Usuario aceptado")
    
    # Prueba para chequear que un usuario registro puede acceder al sistema
    def testIngresoUser(self):
        self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3bA1", "pru3bA1")
        self.assertEqual(self.validacion.ingresarUsuario("costi.abarca@gmail.com", "pru3bA1"), "Usuario aceptado")
    
    # Prueba para chequear que se deniega el acceso si usuario no existe 
    def testAccesoDenegado(self):
        self.assertEqual(self.validacion.ingresarUsuario("usuarionoexiste@gmail.com", "pru3bA1"), "Usuario invalido")

# Pruebas frontera

    # Prueba para chequear que el registro falla si el largo de la contraseña esta justo por encima del max
    def testPassLargoIncorrecto(self):
        self.assertEqual(self.validacion.ingresarUsuario("costi.abarca@gmail.com", "pru3bA78901234567"), "Clave invalida")
    
    # Prueba para chequear que el registro falla si el correo es invalido  
    
    def testCorreoIncorrecto(self):
        self.assertEqual(self.validacion.ingresarUsuario("constazagmail.com", "pru3bA789012345678"), "Correo electronico invalido")
    
    # Prueba para chequear que el registro falla si contraseña tiene caracter especial
    
    def testCaracterEsp(self):
        self.assertEqual(self.validacion.ingresarUsuario("costi@gmail.com", "pru3bA7890.2345678"), "Clave invalida")
    
    # Prueba para chequear que el registro falla si la contraseña no tiene numeros
    def testCaracterEsp(self):
        self.assertEqual(self.validacion.ingresarUsuario("costi@gmail.com", "falTaNumero"), "Clave invalida")
    
    # Prueba para chequear que el registro falla si la contraseña le falta una letra
    def testCaracterEsp(self):
        self.assertEqual(self.validacion.ingresarUsuario("costi@gmail.com", "Ab123456789"), "Clave invalida")