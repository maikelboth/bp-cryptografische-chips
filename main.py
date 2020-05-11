import argparse
import random
from Speck.src.Speck import BP_Speck
from Speck.src.Math import BP_Math


def main(options):
    key = 0x0f0e0d0c0b0a09080706050403020100
    plaintext = 0x6c617669757165207469206564616d20
    register_i = 0
    register_pos = int(options.register_position)
    initial_register_value = random.getrandbits(128)

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

    hamming_distance_leakage = False
    hamming_weight_leakage = False

    for i in range(int(options.amount) - 1):
        new_initial_register_value = random.getrandbits(128)
        cipher.set_initial_register_value(new_initial_register_value)
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

        if abs(t_test_hamming_distance) > 4.5 and not hamming_distance_leakage:
            hamming_distance_leakage = True
            print("Hamming distance leakage at ", i, " traces.")

        if abs(t_test_hamming_weight) > 4.5 and not hamming_weight_leakage:
            hamming_weight_leakage = True
            print("Hamming weight leakage at ", i, " traces.")

        if hamming_weight_leakage and hamming_distance_leakage:
            break

    fixed_math.get_plot_t_test(t_test_list_hamming_distance, t_test_list_hamming_weight)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--amount", help="Max amount of iterations", required=True)
    parser.add_argument("-rp", '--register_position', help="Register position", required=False, default=0)
    opts = parser.parse_args()

    main(opts)
