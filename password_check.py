# Day 3: Final Rating System
password = input("Enter a password to test: ")

score = 0

if len(password) >= 8:
    score = score + 1

has_number = False
for character in password:
    if character.isdigit():
        has_number = True

if has_number:
    score = score + 1

# --- New Day 3 Logic: Evaluate the final score ---
print("\n--- RESULTS ---")
if score == 2:
    print("Rating: STRONG PASSWORD 💪")
elif score == 1:
    print("Rating: MEDIUM PASSWORD ⚠️")
else:
    print("Rating: WEAK PASSWORD ❌") 
