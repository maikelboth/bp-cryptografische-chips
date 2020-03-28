class BP_Speck:
    # Valid setups for the Speck cipher, format = block_size: {key_size: rounds}
    # Source: https://en.wikipedia.org/wiki/Speck_(cipher)
    __valid_setups = {32: {64: 22},
                      48: {72: 22, 96: 23},
                      64: {96: 26, 128: 27},
                      96: {96: 28, 144: 29},
                      128: {128: 32, 192: 33, 256: 34}}

    def __init__(self, key, key_size, block_size, register_pos=0):
        try:
            self.key = key & ((2 ** key_size) - 1)
            self.key_size = key_size
            self.block_size = block_size
            self.register_pos = register_pos
            self.word_size = block_size >> 1
            self.rounds = self.__valid_setups[block_size][key_size]
        except KeyError:
            print("Invalid key size and block size combination!")
        except (ValueError, TypeError):
            print("Invalid key value!")

        self.register_values = []
        self.word_mask = (2 ** self.word_size) - 1

        if self.word_size == 16:
            self.shift_left_amount = 2
            self.shift_right_amount = 7
        else:
            self.shift_left_amount = 3
            self.shift_right_amount = 8

        self.number_of_keywords = self.key_size // self.word_size
        self.key_list_2 = [self.key & self.word_mask]
        self.key_list_1 = []
        for i in range(1, self.number_of_keywords):
            self.key_list_1.append((self.key >> (i * self.word_size)) & self.word_mask)

        # Generate key list
        # Source: https://eprint.iacr.org/2013/404.pdf page 20
        for i in range(self.rounds - 1):
            key_1_shift_right = self._right_rotate(self.key_list_1[i], self.shift_right_amount)
            key_1_plus_key_2 = (key_1_shift_right + self.key_list_2[i]) & self.word_mask
            key_1_final = key_1_plus_key_2 ^ i
            self.key_list_1.append(key_1_final)
            key_2_shift_left = self._left_rotate(self.key_list_2[i], self.shift_left_amount)
            key_2_final = key_2_shift_left ^ key_1_final
            self.key_list_2.append(key_2_final)

    def _right_rotate(self, number, amount):
        return ((number << (self.word_size - amount)) + (number >> amount)) & self.word_mask

    def _left_rotate(self, number, amount):
        return ((number >> (self.word_size - amount)) + (number << amount)) & self.word_mask

    def get_register_values(self):
        return self.register_values

    def encrypt(self, plaintext):
        # Empty earlier register values
        self.register_values = []

        try:
            encrypt_word_1 = (plaintext >> self.word_size) & self.word_mask
            encrypt_word_2 = plaintext & self.word_mask
        except TypeError:
            print("Invalid plaintext value!")
            raise

        for i in range(self.rounds):
            encrypt_word_1_shift_right = self._right_rotate(encrypt_word_1, self.shift_right_amount)
            encrypt_word_1_plus_encrypt_word_2 = (encrypt_word_1_shift_right + encrypt_word_2) & self.word_mask
            encrypt_word_1 = encrypt_word_1_plus_encrypt_word_2 ^ self.key_list_2[i]
            encrypt_word_2_shift_left = self._left_rotate(encrypt_word_2, self.shift_left_amount)
            encrypt_word_2 = encrypt_word_2_shift_left ^ encrypt_word_1

            registers = {0: encrypt_word_1_shift_right,
                         1: encrypt_word_1_plus_encrypt_word_2,
                         2: encrypt_word_1,
                         3: encrypt_word_2_shift_left,
                         4: encrypt_word_2}
            self.register_values.append(registers.get(self.register_pos, 0))

        ciphertext = (encrypt_word_1 << self.word_size) + encrypt_word_2
        return ciphertext

