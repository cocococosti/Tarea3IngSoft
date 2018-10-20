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

    def testCalculoSemanas(self):