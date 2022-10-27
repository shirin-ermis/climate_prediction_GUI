import unittest
import climpred as cp

class AlbedoTest(unittest.TestCase):


    def test_albedo(self):
        albedo = cp.get_albedo(0.73)
        self.assertEqual(albedo, 0.5637)


if __name__ == "__main__":
    unittest.main()
