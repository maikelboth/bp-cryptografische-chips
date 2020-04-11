from unittest import TestCase
from Speck.src.Math import BP_Math


class TestBPMath(TestCase):

    def setUp(self):
        self.register_values = [1, 2, 3, 4]
        self.block_size = 3

    def tearDown(self):
        pass

    def test_hamming_distance_returns_correct_values(self):
        math = BP_Math(self.register_values, self.block_size)
        hamming_distance = math.get_hamming_distance()

        self.assertEqual(2, hamming_distance[0])
        self.assertEqual(1, hamming_distance[1])
        self.assertEqual(3, hamming_distance[2])

    def test_hamming_weight_returns_correct_values(self):
        math = BP_Math(self.register_values, self.block_size)
        hamming_weight = math.get_hamming_weight()

        self.assertEqual(1, hamming_weight[0])
        self.assertEqual(1, hamming_weight[1])
        self.assertEqual(2, hamming_weight[2])
        self.assertEqual(1, hamming_weight[3])

