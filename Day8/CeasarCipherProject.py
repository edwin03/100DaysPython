alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
cont = "yes"

def caesar(direction, text, shift):
	if direction == "encode":
		encrypt(text, shift)
	elif direction == "decode":
		decrypt(text, shift)
	else:
		print("Not a valid input, try again!")

def encrypt(original_text, shift_amount):
	tshift = 0
	encoded_message = ""
	for char in original_text:
		if char in alphabet:
			tshift = alphabet.index(char) + shift_amount
			if tshift > 25:
				tshift = tshift%26
				encoded_message += alphabet[tshift]
			else:
				encoded_message += alphabet[tshift]
		else:
			encoded_message += char
	print(f"Here is the encoded message: {encoded_message}")

def decrypt(original_text, shift_amount):
	decoded_message = ""
	for char in original_text:
		if char in alphabet:
			tshift = alphabet.index(char) - shift_amount
			tshift %= 26
			decoded_message += alphabet[tshift]
		else:
			decoded_message += char

	print(f"Here is the decoded message: {decoded_message}")

while cont == "yes":
	print(logo)
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(direction, text, shift)
	cont = input(f"Type yes if you want to go again. Otherwise, type no:\n").lower()


