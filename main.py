import argparse
import random
from Speck.src.Speck import BP_Speck
from Speck.src.Math import BP_Math


def main(options):
    cipher = BP_Speck(int(options.key, 0), int(options.keysize), int(options.blocksize))
    ciphertext = cipher.encrypt(int(options.plaintext, 0))
    print("Using key: " + options.key + " to encrypt plaintext: " + options.plaintext)
    print("Ciphertext result: " + hex(ciphertext))

    math = BP_Math(cipher.register_values, int(options.blocksize))
    hamming_distance1 = math.get_hamming_distance()
    print("Hamming distance : " + str(hamming_distance1))

    hamming_weight1 = math.get_hamming_weight()
    print("Hamming weight: " + str(hamming_weight1))

    # math.get_plot_hamming()

    hexdigits = "0123456789ABCDEF"
    random_hex = "".join([hexdigits[random.randint(0, 0xF)] for _ in range(int(int(options.blocksize) / 4))])
    print("random hexnumber is " + random_hex)

    list1_distance = []
    list2_distance = []
    list1_weight = []
    list2_weight = []
    t_test_distance_list = []
    t_test_weight_list = []

    for i in range(100):
        list1_distance.append(hamming_distance1[int(options.register_position)])
        list1_weight.append(hamming_weight1[int(options.register_position)])

        hexdigits = "0123456789ABCDEF"
        random_hex = "".join([hexdigits[random.randint(0, 0xF)] for _ in range(int(int(options.blocksize) / 4))])

        cipher_random = BP_Speck(int(options.key, 0), int(options.keysize), int(options.blocksize))
        ciphertext_random = cipher_random.encrypt(int(random_hex, 16))

        math_random = BP_Math(cipher_random.register_values, int(options.blocksize))
        hamming_distance2 = math_random.get_hamming_distance()
        hamming_weight2 = math_random.get_hamming_weight()

        list2_distance.append(hamming_distance2[2])
        list2_weight.append(hamming_weight2[2])

        if (i != 0):
            t_test_distance = math.welchs_t_test(list1_distance, list2_distance)
            t_test_weight = math.welchs_t_test(list1_weight, list2_weight)

            t_test_distance_list.append(t_test_distance)
            t_test_weight_list.append(t_test_weight)

    # print("t-test distance = " + str(t_test_distance_list) + " and t-test weight = " + str(t_test_weight_list))
    math.get_plot_t_test(t_test_distance_list, t_test_weight_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help="Cipher key", required=True)
    parser.add_argument("-pt", "--plaintext", help="Plaintext to encrypt", required=True)
    parser.add_argument("-ks", "--keysize", help="Key size", required=False, default=128)
    parser.add_argument("-bs", "--blocksize", help="Block size", required=False, default=128)
    parser.add_argument("-rp", '--register_position', help="Register position", required=False, default=2)
    opts = parser.parse_args()

    main(opts)
