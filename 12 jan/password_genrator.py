import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','#','$','%','^','&','*']

print("welcome to password generator")
nr_letters = int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input("how many symbols would you\n"))
nr_numbers = int(input("how many numbers would you like?\n"))

#easy
#password = ""

#for char in range(0,nr_letters):
 #   password += random.choice(letter)

#for char in range(0,nr_symbols):
 #   password += random.choice(symbol)

#for char in range(0,nr_numbers):
 #   password += random.choice(numbers)

#print(password)

#hard level
password_list= []
for char in range(0,nr_letters):
    password_list.append(random.choice(letter))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbol))

for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is: {password}")