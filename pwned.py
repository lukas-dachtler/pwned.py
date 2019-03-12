import sys
import hashlib
import requests
password_found = ''
hash_generator = hashlib.sha1()
hash_generator.update(sys.argv[1].encode('utf-8'))
hash_str = hash_generator.hexdigest().upper()
hash_prefix = hash_str[:5]
hash_suffix = hash_str[5:]
req = requests.get('https://api.pwnedpasswords.com/range/' + hash_prefix)
passwords_all = req.text.split()
for p in passwords_all:
	if hash_suffix in p:
		password_found = p
		break
if password_found:
	print ('Password found ' + password_found.split(':')[1] + ' times!')
	print ('Hash: ' + hash_str)
else:
	print ('Password not found!')