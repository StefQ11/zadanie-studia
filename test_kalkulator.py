import unittest
from kalkulator import dodaj, odejmij, pomnoz, podziel

class TestKalkulatora(unittest.TestCase):

    def test_dodaj(self):
        self.assertEqual(dodaj(2, 3), 5)
        self.assertEqual(dodaj(-1, 1), 0)

    def test_odejmij(self):
        self.assertEqual(odejmij(5, 3), 2)
        self.assertEqual(odejmij(1, 2), -1)

    def test_pomnoz(self):
        self.assertEqual(pomnoz(2, 3), 6)
        self.assertEqual(pomnoz(-2, 3), -6)

    def test_podziel(self):
        self.assertEqual(podziel(6, 3), 2)
        self.assertEqual(podziel(5, 2), 2.5)

    def test_podziel_przez_zero(self):
        with self.assertRaises(ValueError):
            podziel(1, 0)

if __name__ == '__main__':
    unittest.main()
