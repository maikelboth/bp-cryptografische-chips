from unittest import TestCase

from src.Speck import BP_Speck


class TestBPSpeck(TestCase):

	def setUp(self):
		self.block_size = 128
		self.key_size = 128
		self.plaintext = 0x6c617669757165207469206564616d20
		self.key = 0x0f0e0d0c0b0a09080706050403020100

	def tearDown(self):
		pass

	def test_register_values_set_correctly(self):
		cipher = BP_Speck(self.key, self.key_size, self.block_size, 4)
		cipher.encrypt(self.plaintext)
		values = cipher.get_register_values()

		self.assertEqual(3502261146266613382, values[0])
		self.assertEqual(423162373122964573, values[1])
		self.assertEqual(11927535118356120913, values[2])
		# ...

	def test_encrypt_returns_correct_hexed_values(self):
		cipher = BP_Speck(self.key, self.key_size, self.block_size, 4)
		ciphertext = cipher.encrypt(self.plaintext)

		self.assertEqual("0xf0e0d0c0b0a09080706050403020100", hex(cipher.key))
		self.assertEqual("0x6c617669757165207469206564616d20", hex(self.plaintext))
		self.assertEqual("0xa65d9851797832657860fedf5c570d18", hex(ciphertext))