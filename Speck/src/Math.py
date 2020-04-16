from matplotlib import pyplot as plt


class BP_Math:

    def __init__(self, register_values, block_size):
        if not isinstance(register_values, list):
            raise TypeError("Register values must be an array")
        if len(register_values) == 0:
            raise ValueError("Register values is an empty list")

        if not isinstance(block_size, int):
            raise TypeError("Block size must be an integer")
        if block_size <= 0:
            raise ValueError("Block size must be a positive integer")

        self.register_values = register_values
        self.block_size = block_size

    def get_hamming_distance(self):
        hamming_distance = []
        for i in range(len(self.register_values) - 1):
            distance = 0
            xor = self.register_values[i] ^ self.register_values[i + 1]

            for j in range(self.block_size):
                xor_bit = (xor >> j) & 1
                if xor_bit == 1:
                    distance += 1
            hamming_distance.append(distance)

        return hamming_distance

    def get_hamming_weight(self):
        hamming_weight = []
        for register_value in self.register_values:
            weight = 0

            for i in range(self.block_size):
                bit = (register_value >> i) & 1
                if bit == 1:
                    weight += 1
            hamming_weight.append(weight)

        return hamming_weight

    def get_plot(self):
        x_rounds_hamming_weight = []
        x_rounds_hamming_distance = []

        for i in range(len(self.register_values)):
            x_rounds_hamming_weight.append(i)

        for i in range(len(self.register_values) - 1):
            x_rounds_hamming_distance.append(i+1)

        plt.plot(x_rounds_hamming_distance, self.get_hamming_distance(), label='hamming distance')
        plt.plot(x_rounds_hamming_weight, self.get_hamming_weight(), label='hamming weight')

        plt.xlabel('rounds')
        plt.ylabel('number of bits')
        plt.legend()

        plt.grid()
        plt.show()
