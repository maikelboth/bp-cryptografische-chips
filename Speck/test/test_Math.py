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

    def test_incorrect_register_values_raises_type_error(self):
        self.assertRaises(TypeError, BP_Math, "test", 1)
        self.assertRaises(TypeError, BP_Math, 1, 1)

    def test_incorrect_block_size_raises_type_error(self):
        self.assertRaises(TypeError, BP_Math, [1], [1])
        self.assertRaises(TypeError, BP_Math, [1], "test")

    def test_empty_register_values_raises_value_error(self):
        self.assertRaises(ValueError, BP_Math, [], 1)

    def test_negative_block_size_raises_value_error(self):
        self.assertRaises(ValueError, BP_Math, [1], -1)

    def test_welchs_t_test_returns_correct_value(self):
        list1 = [27.5, 21.0, 19.0, 23.6, 17.0, 17.9, 16.9, 20.1, 21.9, 22.6, 23.1, 19.6, 19.0, 21.7, 21.4]
        list2 = [27.1, 22.0, 20.8, 23.4, 23.4, 23.5, 25.8, 22.0, 24.8, 20.2, 21.9, 22.1, 22.9, 20.5, 24.4]
        correct_t_value = -2.46

        math = BP_Math(self.register_values)
        t_value = math.welchs_t_test(list1, list2)
        self.assertEqual(correct_t_value, round(t_value, 2))

        list1 = [17.2, 20.9, 22.6, 18.1, 21.7, 21.4, 23.5, 24.2, 14.7, 21.8]
        list2 = [21.5, 22.8, 21.0, 23.0, 21.6, 23.6, 22.5, 20.7, 23.4, 21.8, 20.7, 21.7, 21.5, 22.5, 23.6, 21.5, 22.5, 23.5, 21.5, 21.8]
        correct_t_value = -1.57

        t_value = math.welchs_t_test(list1, list2)
        self.assertEqual(correct_t_value, round(t_value, 2))
