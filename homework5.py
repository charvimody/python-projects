password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1

for ch in password:
    if ch.isupper():
        score += 1
        break

for ch in password:
    if ch.islower():
        score += 1
        break

for ch in password:
    if ch.isdigit():
        score += 1
        break

if score <= 1:
    print("Password Strength: Weak")

elif score <= 3:
    print("Password Strength: Medium")

else:
    print("Password Strength: Strong")