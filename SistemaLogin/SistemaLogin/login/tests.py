from django.test import TestCase

# Create your tests here.

from validation import *
import unittest

class testValidation(unittest.TestCase):
    
    def setUp(self):
        self.pension = Pension()

# Pruebas interiores

    def testCalculoSemanas(self):
        self.assertEqual(self.pension.calcularSemanas(5, 4, 1990), 1488, "Se deben obtener 1488 semanas.")