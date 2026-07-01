#Day 1: Basic Length  Check
password = input("Enter a password to test:")

score = 0

if len(password) >= 8:
	print("[+] Good: Password is 8 or more characters.")
	score = score + 1
else:
	print("[-] Weak: Password is too short (less than 8 characters).")

print(f"Your final security score is: {score}/1")

