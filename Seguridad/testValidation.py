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
    
    