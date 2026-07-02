# Day 2: Length + Number Check
password = input("Enter a password to test: ")

score = 0
total_checks = 2

# Check 1: Length
if len(password) >= 8:
    score = score + 1

# Check 2: Does it contain a number?
has_number = False
for character in password:
    if character.isdigit():  # This checks if the character is a number (0-9)
        has_number = True

if has_number == True:
    print("[+] Good: Password contains at least one number.")
    score = score + 1
else:
    print("[-] Weak: Missing a number.")

print(f"Your final security score is: {score}/{total_checks}")

