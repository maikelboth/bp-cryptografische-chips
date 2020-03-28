
import argparse
from Speck.src.Speck import BP_Speck


def main(options):
	cipher = BP_Speck(int(options.key, 0), options.keysize, options.blocksize)
	ciphertext = cipher.encrypt(int(options.plaintext, 0))
	print("Using key: " + options.key + " to encrypt plaintext: " + options.plaintext)
	print("Ciphertext result: " + hex(ciphertext))


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-k", "--key", help="Cipher key", required=True)
	parser.add_argument("-pt", "--plaintext", help="Plaintext to encrypt", required=True)
	parser.add_argument("-ks", "--keysize", help="Key size", required=False, default=128)
	parser.add_argument("-bs", "--blocksize", help="Block size", required=False, default=128)
	opts = parser.parse_args()

	main(opts)
