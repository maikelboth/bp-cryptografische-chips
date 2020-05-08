import argparse
from Speck.src.Speck import BP_Speck
from Speck.src.Math import BP_Math


def main(options):
    # cipher = BP_Speck(int(options.key, 0), int(options.keysize), int(options.blocksize))
    # ciphertext = cipher.encrypt(int(options.plaintext, 0))
    # print("Using key: " + options.key + " to encrypt plaintext: " + options.plaintext)
    # print("Ciphertext result: " + hex(ciphertext))
    #
    # math = BP_Math(cipher.register_values, int(options.blocksize))
    # hamming_distance1 = math.get_hamming_distance()
    # print("Hamming distance : " + str(hamming_distance1))
    #
    # hamming_weight1 = math.get_hamming_weight()
    # print("Hamming weight: " + str(hamming_weight1))
    #
    # math.get_plot_hamming()

    key = 0x0f0e0d0c0b0a09080706050403020100
    plaintext = 0x6c617669757165207469206564616d20
    register_i = 0
    register_pos = int(options.register_position)
    initial_register_value = int(options.initial_value)

    cipher = BP_Speck(key, 128, 128, register_pos, initial_register_value)
    ciphertext = cipher.encrypt(plaintext)

    fixed_math = BP_Math(cipher.register_values, 128)
    fixed_hamming_distance = fixed_math.get_hamming_distance()[register_i]
    fixed_hamming_weight = fixed_math.get_hamming_weight()[register_i]

    fixed_list_hamming_distance = [fixed_hamming_distance]
    fixed_list_hamming_weight = [fixed_hamming_weight]
    random_list_hamming_distance = [fixed_hamming_distance]
    random_list_hamming_weight = [fixed_hamming_weight]

    t_test_list_hamming_distance = []
    t_test_list_hamming_weight = []

    for i in range(int(options.amount)-1):
        ciphertext = cipher.encrypt(ciphertext)
        random_math = BP_Math(cipher.register_values, 128)
        random_hamming_distance = random_math.get_hamming_distance()[register_i]
        random_hamming_weight = random_math.get_hamming_weight()[register_i]

        fixed_list_hamming_distance.append(fixed_hamming_distance)
        fixed_list_hamming_weight.append(fixed_hamming_weight)
        random_list_hamming_distance.append(random_hamming_distance)
        random_list_hamming_weight.append(random_hamming_weight)

        t_test_hamming_distance = fixed_math.welchs_t_test(fixed_list_hamming_distance, random_list_hamming_distance)
        t_test_hamming_weight = fixed_math.welchs_t_test(fixed_list_hamming_weight, random_list_hamming_weight)

        t_test_list_hamming_distance.append(t_test_hamming_distance)
        t_test_list_hamming_weight.append(t_test_hamming_weight)

        if abs(t_test_hamming_distance) > 4.5 or abs(t_test_hamming_weight) > 4.5:
            print("Information leakage at ", i, " traces")
            break

    fixed_math.get_plot_t_test(t_test_list_hamming_distance, t_test_list_hamming_weight)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("-k", "--key", help="Cipher key", required=True)
    # parser.add_argument("-pt", "--plaintext", help="Plaintext to encrypt", required=True)
    # parser.add_argument("-ks", "--keysize", help="Key size", required=False, default=128)
    # parser.add_argument("-bs", "--blocksize", help="Block size", required=False, default=128)
    parser.add_argument("-a", "--amount", help="Max amount of iterations", required=True)
    parser.add_argument("-rp", '--register_position', help="Register position", required=False, default=0)
    parser.add_argument("-iv", "--initial_value", help="Initial register value", required=False, default=0)
    opts = parser.parse_args()

    main(opts)
