import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy version:
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
# 4 letters 2 symbols and 3 numbers then the password might look like this:
# fgdx$*924
# You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well.
easy_password = []
for l in range(1, nr_letters+1):
    easy_password.append(random.choice(letters))
for s in range(1, nr_symbols+1):
    easy_password.append(random.choice(symbols))
for n in range(1, nr_numbers+1):
    easy_password.append(random.choice(numbers))

print(f"Your easy password is: {''.join(easy_password)}")

# Hard version:
# In the advanced version of this project the final password does not follow a pattern.
# So the example above might look like this:
# x$d24g*f9
# And every time you generate a password, the positions of the symbols, numbers, and letters are different.
# This will make the password more difficult for hackers to crack.
random.shuffle(easy_password)
hard_password = "".join(easy_password)
print(f"Your hard password is: {hard_password}")
