import unittest
import climpred as cp


class TestTemperatureVector(unittest.TestCase):

    def test_empty_layers(self):
        layers = ['']
        epsilons = ['']
        H = ['']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 1)

    def test_empty_epsilons(self):
        layers = ['1']
        epsilons = ['']
        H = ['']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 2)

    def test_empty_H(self):
        layers = ['2']
        epsilons = ['0.5 0.6']
        H = ['']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 3)

    def test_layer_not_int(self):
        layers = ['a']
        epsilons = ['0.5 0.6']
        H = ['0.5 0.5']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 4)

    def test_epsilons_not_transformable(self):
        layers = ['2']
        epsilons = ['0.5, 0.6']
        H = ['0.5 0.5']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 5)

    def test_H_not_transformable(self):
        layers = ['2']
        epsilons = ['0.5 0.6']
        H = ['0.5A0.5']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 6)

    def test_too_few_layers(self):
        layers = ['0']
        epsilons = ['0.5 0.6']
        H = ['0.5 0.5']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 7)

    def test_epsilon_not_in_range(self):
        layers = ['2']
        epsilons = ['1.5 0.6']
        H = ['50 60']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 8)

    def test_negative_H(self):
        layers = ['2']
        epsilons = ['0.5 0.6']
        H = ['-50 60']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 9)

    def test_no_epsilons_inconsistent(self):
        layers = ['3']
        epsilons = ['0.5 0.6']
        H = ['50 60']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 10)

    def test_no_H_inconsistent(self):
        layers = ['2']
        epsilons = ['0.5 0.6']
        H = ['50 60 60']

        self.assertEqual(cp._check_inputs(layers, epsilons, H,
                                          type_run='TEST'), 11)


if __name__ == '__main__':
    unittest.main()
