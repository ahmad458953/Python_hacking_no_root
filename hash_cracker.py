import hashlib
hash = input("enter your hash ")
passls = input("pls enter pass list ")
try:
	with open(passls, "r") as f:
		for guess in f:
			guess = guess.strip()
			hashed = hashlib.md5(guess.encode()).hexdigest()
			if hashed == hash:
				print(f"[+] password found: {guess}")
				break
			else:
				print(f"[/] password not found")
except FileNotFoundError:
	print(f"[-] pass list file not found")
