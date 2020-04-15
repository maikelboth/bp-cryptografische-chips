from unittest import TestCase
from Speck.src.Speck import BP_Speck


class TestBPSpeck(TestCase):

	def setUp(self):
		self.block_size = 128
		self.key_size = 128
		self.plaintext = 0x6c617669757165207469206564616d20
		self.key = 0x0f0e0d0c0b0a09080706050403020100
		self.register_pos = 4
		self.default_register_value = 15

	def tearDown(self):
		pass

	def test_register_values_set_correctly(self):
		cipher = BP_Speck(self.key, self.key_size, self.block_size, self.register_pos, self.default_register_value)
		cipher.encrypt(self.plaintext)
		values = cipher.get_register_values()

		self.assertEqual(self.default_register_value, values[0])
		self.assertEqual(3502261146266613382, values[1])
		self.assertEqual(423162373122964573, values[2])
		self.assertEqual(11927535118356120913, values[3])
		self.assertEqual(13086198756631555644, values[4])
		self.assertEqual(14602580204519412693, values[5])
		self.assertEqual(2000143021029299983, values[6])
		self.assertEqual(13867416285273009822, values[7])
		self.assertEqual(5771282879215514673, values[8])
		self.assertEqual(14168928477211072166, values[9])
		self.assertEqual(6350807575834690766, values[10])
		self.assertEqual(2578544979115758229, values[11])
		self.assertEqual(6977039667070824382, values[12])
		self.assertEqual(441122036121552369, values[13])
		self.assertEqual(13831654436958558579, values[14])
		self.assertEqual(17069271371720262406, values[15])
		self.assertEqual(12148416450501388288, values[16])
		self.assertEqual(15260204053528369830, values[17])
		self.assertEqual(126441440922855510, values[18])
		self.assertEqual(9991915174888376624, values[19])
		self.assertEqual(1373025304360913802, values[20])
		self.assertEqual(7303535335452223808, values[21])
		self.assertEqual(17050466197131240311, values[22])
		self.assertEqual(15133961284916196885, values[23])
		self.assertEqual(5666866483476972917, values[24])
		self.assertEqual(13802561923659999880, values[25])
		self.assertEqual(8747893489135413107, values[26])
		self.assertEqual(129179017315910753, values[27])
		self.assertEqual(15424141043077198385, values[28])
		self.assertEqual(9739864489950961510, values[29])
		self.assertEqual(9866432828159742340, values[30])
		self.assertEqual(13530973622405294063, values[31])
		self.assertEqual(8674213117595946264, values[32])

	def test_encrypt_returns_correct_hexed_values(self):
		cipher = BP_Speck(self.key, self.key_size, self.block_size, 4)
		ciphertext = cipher.encrypt(self.plaintext)

		self.assertEqual("0xf0e0d0c0b0a09080706050403020100", hex(cipher.key))
		self.assertEqual("0x6c617669757165207469206564616d20", hex(self.plaintext))
		self.assertEqual("0xa65d9851797832657860fedf5c570d18", hex(ciphertext))

	def test_incorrect_key_raises_type_error(self):
		self.assertRaises(TypeError, BP_Speck, "test", 1, 1)
		self.assertRaises(TypeError, BP_Speck, [1], 1, 1)

	def test_incorrect_key_size_raises_type_error(self):
		self.assertRaises(TypeError, BP_Speck, 1, "test", 1)
		self.assertRaises(TypeError, BP_Speck, 1, [1], 1)

	def test_incorrect_block_size_raises_type_error(self):
		self.assertRaises(TypeError, BP_Speck, 1, 1, "test")
		self.assertRaises(TypeError, BP_Speck, 1, 1, [1])

	def test_incorrect_register_pos_raises_type_error(self):
		self.assertRaises(TypeError, BP_Speck, 1, 1, 1, "test")
		self.assertRaises(TypeError, BP_Speck, 1, 1, 1, [1])

	def test_incorrect_key_size_raises_key_error(self):
		self.assertRaises(KeyError, BP_Speck, self.key, 0, self.block_size)

	def test_incorrect_block_size_raises_key_error(self):
		self.assertRaises(KeyError, BP_Speck, self.key, self.key_size, 0)

	def test_incorrect_key_size_block_size_combination_raises_key_error(self):
		self.assertRaises(KeyError, BP_Speck, self.key, 32, 72)

	def test_incorrect_plaintext_raises_type_error(self):
		speck = BP_Speck(self.key, self.key_size, self.block_size)
		self.assertRaises(TypeError, speck.encrypt, "test")
