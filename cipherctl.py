#!/usr/local/bin/python3

import argparse
import re
import string

def atbash(message):
	""" Method is used for encoding or decoding the plaintext """

	# Our dictionary that maps the alphabet to the reverse letter
	lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

	# Variable to hold our encode/decoded value
	cipher = ""

	# We loop through all letters in our message variable to get the equivalent reverse
	for letter in message.upper():

		# We make sure to check for spaces, if none exist we encode/decode otherwise we add a space
		if letter != " ":
			cipher += lookup_table[letter]
		else:
			cipher += " "

	return cipher


def run():
	""" Main method for running the program """

	# Main parser 
	parser = argparse.ArgumentParser(description="The cipherctl utility allows you to encode or decode in various ciphers")
	parser.add_argument("-t", "--type", required=True, type=str, choices=["atbash","rot13","caesar","vigenere"])
	parser.add_argument("-m", "--message", required=True, type=str)


	args = parser.parse_args()

	if args.type == "atbash":
		result = atbash(args.message)
		print(result)


if __name__ == '__main__':
	run()

