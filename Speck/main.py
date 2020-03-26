
import argparse

def main(options):
	print("doing stuff with options bla: " + options.bla + " and blie: " + options.blie)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-b", "--bla", help="option numbero uno", required=True)
	parser.add_argument("-l", "--blie", help="other shizzle, option blie",required=False)
	opts = parser.parse_args()

	main(opts)