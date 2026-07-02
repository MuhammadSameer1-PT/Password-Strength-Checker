password = input("Enter your password: ")

if len(password) >= 8:
    print("Password length is good.")
else:
    print("Password is too short.")

has_upper = False

for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    print("Password contains an uppercase letter.")
else:
    print("Password does not contain an uppercase letter.")

has_number = False

for char in password:
    if char.isdigit():
        has_number = True
        break

if has_number:
    print("Password contains a number.")
else:
    print("Password does not contain a number.")

has_symbol = False

symbols = "!@#$%^&*"

for char in password:
    if char in symbols:
        has_symbol = True
        break

if has_symbol:
    print("Password contains a special character.")
else:
    print("Password does not contain a special character.") 

score = 0

if len(password) >= 8:
    score += 1

if has_upper:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1

if score <= 1:
    print("\nPassword Strength: Weak")

elif score <= 3:
    print("\nPassword Strength: Medium")

else:
    print("\nPassword Strength: Strong")    