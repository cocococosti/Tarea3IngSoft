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
        self.assertEqual(self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3bA12", "pru3bA12"), "Usuario aceptado")
    
    # Prueba para chequear que un usuario registro puede acceder al sistema
    def testIngresoUser(self):
        self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3bA12", "pru3bA12")
        self.assertEqual(self.validacion.ingresarUsuario("costi.abarca@gmail.com", "pru3bA12"), "Usuario aceptado")
    
    # Prueba para chequear que se deniega el acceso si usuario no existe 
    def testAccesoDenegado(self):
        self.assertEqual(self.validacion.ingresarUsuario("usuarionoexiste@gmail.com", "pru3bA1"), "Usuario invalido")

# Pruebas frontera

    # Prueba para chequear que el registro falla si el largo de la contraseña esta justo por encima del max
    def testPassLargoIncorrecto(self):
        self.assertEqual(self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3bA78901234567",  "pru3bA78901234567"), "Clave invalida")
    
    # Prueba para chequear que el registro falla si el correo es invalido  
    
    def testCorreoIncorrecto(self):
        self.assertEqual(self.validacion.registrarUsuario("constazagmail.com", "pru3bA789012345678", "pru3bA789012345678"), "Correo electronico invalido")
    
    # Prueba para chequear que el registro falla si contraseña tiene caracter especial
    
    def testCaracterEsp(self):
        self.assertEqual(self.validacion.registrarUsuario("costi@gmail.com", "pru3bA7890.2345678", "pru3bA7890.2345678"), "Clave invalida")
    
    # Prueba para chequear que el registro falla si la contraseña no tiene numeros
    def testNoNum(self):
        self.assertEqual(self.validacion.registrarUsuario("costi@gmail.com", "falTaNumero", "falTaNumero"), "Clave invalida")
    
    # Prueba para chequear que el registro falla si la contraseña le falta una letra
    def testFaltaLetra(self):
        self.assertEqual(self.validacion.registrarUsuario("costiabarca@gmail.com", "ab123456789", "ab123456789"), "Clave invalida")

# Pruebas esquina
    
    def testPassIncorrecto(self):
        self.validacion.registrarUsuario("denylson97@gmail.com", "pru3bA12", "pru3bA12")
        self.assertEqual(self.validacion.ingresarUsuario("denylson97@gmail.com", "pru3bA1"), "Clave invalida")
    
    def testPassInvalido(self):
        self.validacion.registrarUsuario("denylson97@gmail.com", "pru3bA12", "pru3bA12")
        self.assertEqual(self.validacion.ingresarUsuario("denylson97@gmail.com", "incorrecT0"), "Clave invalida")
    
    def testDatosInv(self):
        self.assertEqual(self.validacion.registrarUsuario("costiabarcagmai", "pr", "pr"), "Correo electronico invalido")
    
# Pruebas malicia
    
    def testYaExiste(self):
        self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3bA12", "pru3bA12")
        self.assertEqual(self.validacion.registrarUsuario("costi.abarca@gmail.com", "pru3b33A1", "pru3b33A1"), "Correo electronico invalido")
    
    def testRegistroVacio(self):
        self.assertEqual(self.validacion.registrarUsuario("", "", ""), "Correo electronico invalido")
    
    def testIngresoVacio(self):
        self.assertEqual(self.validacion.ingresarUsuario("", ""), "Correo electronico invalido")
        
        
        
        