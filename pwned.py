import sys
import hashlib
import requests
import os.path

# Function for checking if the given password has been compromised
def check_password(password):
	password_found = ''
	hash_generator = hashlib.sha1()
	hash_generator.update(password)
	# Generate SHA1
	hash_str = hash_generator.hexdigest().upper()
	hash_prefix = hash_str[:5]
	hash_suffix = hash_str[5:]
	# Only send the first 5 characters (prefix) to the API
	req = requests.get('https://api.pwnedpasswords.com/range/' + hash_prefix)
	passwords_result = req.text.split()
	# Search for the corresponding suffix from the results
	for p in passwords_result:
		if hash_suffix in p:
			return p
	return ''

# Get command-line argument
input_str = sys.argv[1]
# Check if parameter is a file
if '.txt' in input_str:
	# Check if file exists
	if os.path.isfile(input_str):
		# Read file
		with open(input_str, 'r') as file:
			passwords_check = file.readlines()
		i = 0
		# Iterate over each password to be tested
		while i < len(passwords_check):
			passwords_check[i] = passwords_check[i].rstrip()
			# Check password
			result = check_password(passwords_check[i].encode('utf-8'))
			# Update line to show result
			if result:
				passwords_check[i] += " - found " + result.split(':')[1] + ' times!\n'
			else:
				passwords_check[i] += " - not found!\n"
			i += 1
		# Write file with updated lines
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