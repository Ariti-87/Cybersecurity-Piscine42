from cryptography.fernet import Fernet
import os
import sys
import hmac
import time
import struct
import hashlib
import base64

def store_key(keyfile):
	"""Encrypts and stores the key in a file."""

	with open(keyfile, 'r') as file:
		hex_key = file.read().strip()

	if len(hex_key) != 64 or not all(c in '0123456789abcdefABCDEF' for c in hex_key):
		print("Error: key must be 64 hexadecimal characters.")
		return

	encryption_key = Fernet.generate_key()
	cipher_suite = Fernet(encryption_key)
	encrypted_key = cipher_suite.encrypt(hex_key.encode())

	with open('ft_otp.key', 'wb') as file:
		file.write(encrypted_key + b'\n' + encryption_key)

	print("Key successfully saved to 'ft_otp.key'.")

def load_key():
	"""Decrypts and loads the key from a file."""

	with open('ft_otp.key', 'rb') as file:
		encrypted_key = file.readline().strip()
		encryption_key = file.readline().strip()

	cipher_suite = Fernet(encryption_key)
	hex_key = cipher_suite.decrypt(encrypted_key).decode()

	return hex_key

def generate_otp():
	"""Generates a OTP token using the stored key."""

	if not os.path.exists('ft_otp.key'):
		print("Error: key file not found.")
		return

	secret = load_key()
	key = bytes.fromhex(secret)

	base32_key = base64.b32encode(key).decode('utf-8')
	print("OATHTOOL 32 key : " + base32_key)

	counter = int(time.time()) // 30
	counter_bytes = struct.pack('>Q', counter)
	hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()


	offset = hmac_hash[-1] & 0xf
	code = struct.unpack('>I', hmac_hash[offset:offset + 4])[0] & 0x7fffffff
	otp = code % 1000000
	print(f"MY OTP : {otp:06}") # Print OTP padded to 6 digits


def main():
	if len(sys.argv) != 3:
		print("Usage: python hotp.py -g <keyfile> or python hotp.py -k ft_otp.key")
		sys.exit(1)

	mode = sys.argv[1]
	file = sys.argv[2]

	if mode == '-g':
		store_key(file)
	elif mode == '-k':
		generate_otp()
	else:
		print("Invalid argument. Use -g to encrypt a key or -k to generate HOTP.")

if __name__ == "__main__":
	main()
