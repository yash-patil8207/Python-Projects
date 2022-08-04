import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the Password generator! ")
nr_letters = int(input("How many letters would you like in your password?\n "))
nr_numbers = int(input(f"How many numbers would you like ? \n"))
nr_symbols = int(input(f"how many symbols would you like? \n"))

password_list = []
for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)
for char in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)
    
print(password_list)
random.shuffle(password_list)
print(password_list) 

password = ""
for char in password_list:
    password += char
print(f"Your Password is: {password}")       
             