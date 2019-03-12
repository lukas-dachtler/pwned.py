import sys
import hashlib
import requests
import os.path

def check_password(password):
	password_found = ''
	hash_generator = hashlib.sha1()
	hash_generator.update(password)
	hash_str = hash_generator.hexdigest().upper()
	hash_prefix = hash_str[:5]
	hash_suffix = hash_str[5:]
	req = requests.get('https://api.pwnedpasswords.com/range/' + hash_prefix)
	passwords_result = req.text.split()
	for p in passwords_result:
		if hash_suffix in p:
			return p
	return ''

input_str = sys.argv[1]
if '.txt' in input_str:
	if os.path.isfile(input_str):
		with open(input_str, 'r') as file:
			passwords_check = file.readlines()
		i = 0
		while i < len(passwords_check):
			passwords_check[i] = passwords_check[i].rstrip()
			result = check_password(passwords_check[i].encode('utf-8'))
			if result:
				passwords_check[i] += " - found " + result.split(':')[1] + ' times!\n'
			else:
				passwords_check[i] += " - not found!\n"
			i += 1
		with open(input_str, 'w') as file:
			file.writelines(passwords_check)
		print ('Completed!')
	else:
		print ('Path not valid!')
else:
	result = check_password(input_str.encode('utf-8'))
	if result:
		print ('Password found ' + result.split(':')[1] + ' times!')
	else:
		print ('Password not found!')