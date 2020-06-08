import unittest
from dokumentarij import Dokumentarij

class DokumentarijTestCase(unittest.TestCase):
    def test_new_names(self):
        game_test = Dokumentarij()
        names = game_test.new_names()
        self.assertEqual(str(names), "U dokumentariju možemo pronaći imena svih studenata")



if __name__ == '__main__':
    unittest.main()