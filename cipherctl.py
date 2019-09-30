#!/usr/local/bin/python3

import argparse
import re
import string
import sys
import logging as logger

DEBUG = False

def atbash_cipher(message):
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

def caesar_cipher(message, shift, action):
	""" Method is used for encoding / decoding the plaintext value using caesar cipher """

	# Our lookup table that converts the upper case letter to a numeric value
	lookup_table = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 
        'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 
        'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 
        'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 
        'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}

	reverse_table = {v: k for k, v in lookup_table.items()}


	cipher = ""

	# We loop through each letter in our message, converting to a number to perform the shift.
	for letter in message.upper():

		# We check for spaces in our message, if none exist, we encode/decode otherwise add a space
		if letter != " ":

			if action == "encode":
				# We first need to take the numeric value that we looked up, apply the shift, mod it, then get the new letter
				new_letter_nbr = lookup_table[letter]
				new_letter_val = (new_letter_nbr + shift) % 26
				cipher += reverse_table[new_letter_val]
			elif action == "decode":
				new_letter_nbr = lookup_table[letter]
				new_letter_val = (new_letter_nbr - shift) % 26
				cipher += reverse_table[new_letter_val]
			else:
				logger.warn("There is no action provided")

		else:
			cipher += " "

	return cipher


def rot13_cipher(message):
	""" Method is responsible for encoding / decoding a message in rot-13 """

	# our lookup table for converting ROT-13 values
	lookup_table = {"A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T", "H": "U", "I": "V", "J": "W", "K": "X", "L": "Y", "M": "Z"}

	# our reverse lookup table for converting backwards for decoding
	reverse_table = {v: k for k, v in lookup_table.items()}

	cipher = ""

	# We loop through the message, converting our letters
	for letter in message.upper():

		
		if letter != " ":
			try:
				cipher += lookup_table[letter]
			except:
				cipher += reverse_table[letter]
		else:
			cipher += " "


	return cipher


def vigenere_cipher(message, keyword, action):
	""" Method is used for encoding / decoding a message using the vigenere cipher """
	global DEBUG

	def _alphabet_table(letter):
		""" sub method to perform character to nbr conversions """
		# Our lookup table that converts the upper case letter to a numeric value
		lookup_table = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 
	        'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 
	        'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 
	        'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 
	        'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}

		position = lookup_table[letter.upper()]

		return position

	def _rotate_(letter, rot):
		""" sub method used for rotating characters """
		shift = 97 if letter.islower() else 65
		return chr((ord(letter) + rot - shift) % 26 + shift)



	cipher = []
	starting_index = 0

	lookup_table = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 
	        'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 
	        'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 
	        'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 
	        'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y' : 24, 'Z' : 25}

	reverse_table = {v: k for k, v in lookup_table.items()}

	if action == "encode":
		# We loop through our message, getting individual letters and converting them to our numeric value
		for letter in message.upper():

			rotation = _alphabet_table(keyword[starting_index])

			if letter != " ":
				if not letter in lookup_table:
					cipher.append(letter)
				elif letter.isalpha():
					cipher.append(_rotate_(letter, rotation))

				if starting_index == (len(keyword) - 1):
					starting_index = 0
				else:
					starting_index += 1
			else:
				cipher.append(" ")

	elif action == "decode":
		# We loop through our message, getting individual letters and converting them to our numeric value
		for letter in message.upper():

			rotation = _alphabet_table(keyword[starting_index])

			if letter != " ":
				subtracted_val = lookup_table[letter] - rotation

				if DEBUG:
					logger.debug("The current letter and rotation number is: {},{}".format(letter, rotation))

				if subtracted_val < 0:
					subtracted_val = subtracted_val + 26

				if DEBUG:
					logger.debug("The substracted value is now: {}".format(subtracted_val))

				cipher.append(reverse_table[subtracted_val])

				if starting_index == (len(keyword) - 1):
					starting_index = 0
				else:
					starting_index += 1
			else:
				cipher.append(" ")

			

	return "".join(cipher)


def run():
	""" Main method for running the program """

	global DEBUG

	# These parser objects control the main parser
	parser = argparse.ArgumentParser(description='The cipherctl utility allows you to encode or decode in various ciphers')	
	parser.add_argument('--debug', help="Enables verbose logging for cipherctl commands", required=False, action="store_true") 
	#parser.add_argument("-t", "--type", required=True, type=str, choices=["atbash","rot13","caesar","vigenere"])

	# Create the parent subparser to be used for other actions
	subparsers = parser.add_subparsers(help="ciphers")

	# create the subparser for our atbash command
	atbash = subparsers.add_parser("atbash", help="Atbash cipher actions", parents=[parser], add_help=False)
	atbash.set_defaults(which="atbash")
	atbash.add_argument("-m", "--message", required=True, type=str)



	# create the subparser for our caesar cipher command
	caesar = subparsers.add_parser("caesar", help="Caesar cipher actions", parents=[parser], add_help=False)
	caesar.add_argument("-a", "--action", required=True, type=str, choices=["encode","decode"])
	caesar.add_argument("-m", "--message", required=True, type=str)
	caesar.add_argument('-s','--shift', help="The amount of shifts to use", required=True, type=int)
	caesar.set_defaults(which="caesar")



	# create the subparser for our rot-13 cipher command
	rot13 = subparsers.add_parser("rot13", help="ROT-13 cipher actions", parents=[parser], add_help=False)
	rot13.add_argument("-m", "--message", required=True, type=str)
	rot13.set_defaults(which="rot13")

	# create the subparser for our vigenere cipher command
	vigenere = subparsers.add_parser("vigenere", help="Vigenere cipher actions", parents=[parser], add_help=False)
	vigenere.add_argument("-a", "--action", required=True, type=str, choices=["encode","decode"])
	vigenere.add_argument("-m", "--message", required=True, type=str)
	vigenere.add_argument("-k", "--keyword", required=True, type=str)
	vigenere.set_defaults(which="vigenere")


	# Parse the args that were given and used
	args = parser.parse_args()

	vars_dict = vars(args)

	try:
		which_parser = vars_dict["which"]
	except Exception as err:
		parser.print_help(sys.stderr)
		sys.exit(1)


	if args.debug:
		DEBUG = True
		logger.basicConfig(level=logger.DEBUG, format='%(asctime)s - %(message)s')
		print(args)
		print(vars(args))


	if args.message:
		if re.search(r"^[a-zA-Z ]+$", args.message):
			if which_parser == "atbash":
				result = atbash_cipher(args.message)
			elif which_parser == "caesar":
				result = caesar_cipher(args.message, args.shift, args.action)
			elif which_parser == "rot13":
				result = rot13_cipher(args.message)
			elif which_parser == "vigenere":
				result = vigenere_cipher(args.message, args.keyword, args.action)
			else:
				logger.warn("no cipher action was found... exiting.")
				sys.exit(0)

			print(result)
		else:
			print("Oops, an invalid character was entered. Please try again.")


if __name__ == '__main__':
	run()

