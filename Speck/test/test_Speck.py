from unittest import TestCase
from Speck.src.Speck import BP_Speck


class TestBPSpeck(TestCase):

	def setUp(self):
		self.block_size = 128
		self.key_size = 128
		self.plaintext = 0x6c617669757165207469206564616d20
		self.key = 0x0f0e0d0c0b0a09080706050403020100
		self.register_pos = 4
		self.initial_register_value = 15

	def tearDown(self):
		pass

	def test_register_values_set_correctly(self):
		cipher = BP_Speck(self.key, self.key_size, self.block_size, self.register_pos, self.initial_register_value)
		cipher.encrypt(self.plaintext)
		values = cipher.get_register_values()

		self.assertEqual(self.initial_register_value, values[0])
		self.assertEqual(196494785027492664489523105407009011334, values[1])
		self.assertEqual(171529479605132456393175388116852030557, values[2])
		self.assertEqual(185416322758900141288527926872067867985, values[3])
		self.assertEqual(204220410083319239821552645534374604348, values[4])
		self.assertEqual(136219465668633803987236843564730667989, values[5])
		self.assertEqual(104965644926602959426510842665758463759, values[6])
		self.assertEqual(40528766305457193263106435016477519518, values[7])
		self.assertEqual(110991068741878491179456181854192743473, values[8])
		self.assertEqual(90551648854263943634611124158952969894, values[9])
		self.assertEqual(166421934508474987935112744463199143118, values[10])
		self.assertEqual(301548365085944936832197405189006676629, values[11])
		self.assertEqual(168260505039421505385613656441329086398, values[12])
		self.assertEqual(686899633740864653588777672541947377, values[13])
		self.assertEqual(190134636038446279611343013419673377139, values[14])
		self.assertEqual(25906813926881664581280199493162205958, values[15])
		self.assertEqual(275846112883781122663509340045105801216, values[16])
		self.assertEqual(201346270259070753434077581996668279462, values[17])
		self.assertEqual(212635593991128713261455825963713062998, values[18])
		self.assertEqual(176308485625654779085278022027115923760, values[19])
		self.assertEqual(93537776552559332650020487641797888906, values[20])
		self.assertEqual(336569374889130958564551543397749664064, values[21])
		self.assertEqual(263548517677336213960331251471141053303, values[22])
		self.assertEqual(243237136964496225511036199709415945749, values[23])
		self.assertEqual(295845673524119198562408776665857934709, values[24])
		self.assertEqual(269389436048049190717605150358116903560, values[25])
		self.assertEqual(176801059830178080887220429542477686643, values[26])
		self.assertEqual(269817576654283530102852091079459374177, values[27])
		self.assertEqual(287585492821841949635478253977628553777, values[28])
		self.assertEqual(73473745069664778162890922853488123750, values[29])
		self.assertEqual(236244422808012408914336476732514029956, values[30])
		self.assertEqual(335813419249842507961391603850427099119, values[31])
		self.assertEqual(221137820289473687857657110085594713368, values[32])

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
