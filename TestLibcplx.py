import Libcplx as lc
import unittest

class TestOperacionesComplejos(unittest.TestCase):

    def test_sumar_complejos(self):
        suma = lc.sumar_complejos((1, 1), (2, 3))
        self.assertAlmostEqual(suma[0], 3)
        self.assertAlmostEqual(suma[1], 4)

    def test_sumar_complejos(self):
        suma = lc.sumar_complejos((0, 0), (-3, 7))
        self.assertAlmostEqual(suma[0], -3)
        self.assertAlmostEqual(suma[1], 7)

    def test_multiplicar_complejos(self):
        multip = lc.multiplicar_complejos((1, 2), (3, 4))
        self.assertAlmostEqual(multip[0], -5)
        self.assertAlmostEqual(multip[1], 10)

    def test_multiplicar_complejos(self):
        multip = lc.multiplicar_complejos((2, -1), (1, -1))
        self.assertAlmostEqual(multip[0], 1)
        self.assertAlmostEqual(multip[1], -3)

    def test_restar_complejos(self):
        resta = lc.restar_complejos((5, 5), (2, 3))
        self.assertAlmostEqual(resta[0], 3)
        self.assertAlmostEqual(resta[1], 2)

    def test_restar_complejos(self):
        resta = lc.restar_complejos((-1, -1), (-3, 2))
        self.assertAlmostEqual(resta[0], 2)
        self.assertAlmostEqual(resta[1], -3)

    def test_dividir_complejos(self):
        div = lc.dividir_complejos((5, 5), (1, 1))
        self.assertAlmostEqual(div[0], 5)
        self.assertAlmostEqual(div[1], 0)

    def test_dividir_complejos(self):
        div = lc.dividir_complejos((2, 3), (-1, 4))
        self.assertAlmostEqual(div[0], 0.58823529)
        self.assertAlmostEqual(div[1], -0.64705882)

    def test_modulo_complejo(self):
        self.assertAlmostEqual(lc.modulo_complejo((3, 4)), 5)

    def test_modulo_complejo(self):
        self.assertAlmostEqual(lc.modulo_complejo((8, 6)), 10)

    def test_conjugado_complejo(self):
        conj = lc.conjugado_complejo((3, 4))
        self.assertAlmostEqual(conj[0], 3)
        self.assertAlmostEqual(conj[1], -4)

    def test_conjugado_complejo(self):
        conj = lc.conjugado_complejo((7, -3))
        self.assertAlmostEqual(conj[0], 7)
        self.assertAlmostEqual(conj[1], 3)

    def test_polar_a_cartesiano(self):
        polar = lc.polar_a_cartesiano((3, 4))
        self.assertAlmostEqual(polar[0], 3)
        self.assertAlmostEqual(polar[1], 4)

    def test_polar_a_cartesiano(self):
        polar = lc.polar_a_cartesiano((6, 8))
        self.assertAlmostEqual(polar[0], 6)
        self.assertAlmostEqual(polar[1], 8)

    def test_fase_complejo(self):
        self.assertAlmostEqual(lc.fase_complejo((3, 4)), 0.927295218)

    def test_fase_complejo(self):
        self.assertAlmostEqual(lc.fase_complejo((7, -3)), -0.404891786)

if __name__ == '__main__':
    unittest.main()
