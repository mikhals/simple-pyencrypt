from simple_aes_cipher import AESCipher, generate_secret_key


cmd = input("(1)encrypt   (2)decrypt  (1/2):")
if cmd == "1":
	text = input("Insert your string to be encrypted:")
	pwd = input("Set password:")
	secret_key = generate_secret_key(pwd)
	cipher = AESCipher(secret_key)

	encrypt_text = cipher.encrypt(text)
	print(encrypt_text)
elif cmd == "2":
	text = input("Insert your string to be decrypted:")
	pwd = input("Set password:")
	secret_key = generate_secret_key(pwd)
	cipher = AESCipher(secret_key)
	decrypt_text = cipher.decrypt(text)
	print(decrypt_text)
else:
	print("Please input 1 or 2")
