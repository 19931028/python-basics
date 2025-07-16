string1 = 'This is a valid string'
string2 = "This is also a valid string"
# string3 = 'This is NOT valid - see why?"

palindrome = "Go hang a salami, I'm a lasagna hog"

#Using quote inside string

string3 = "'Always look on the bright side of life' - Monty Python"
# Using escaped quotes for the nested quote
string4 = "\"Always look on the bright side of life\" - Monty Python"
print(string4)

print(len(string4))

# strip function

name = "    Lia   "
print(len(name))
print(name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print("Hello " + name_no_spaces)

# split()

filepath = "/var/lia/here"
folders = filepath.split("/")
print(folders)
print(type(folders))

# join()
windowsPath = "||".join(folders)
print(windowsPath)

# find()

reservation_name = "Frobman, Abe"
char_to_find = ","

# where is the comma?
char_location = reservation_name.find(char_to_find)
print(char_location)

# index()

char_location = reservation_name.index(char_to_find)
print(char_location)

# transformation

print(reservation_name.upper())
print(reservation_name.lower())
print(reservation_name.title())
print(reservation_name.swapcase())
print(reservation_name.capitalize())

# f-string

name = "Lia"
age = 24
print(f"My name is {name} and I am {age} years old.")
print("My name is"  + name + " and I am " + str(age) + "years old.")

a = 3
b = 9
print(f'we can count to {b} by {a}: {a} {a*2} {a*3}')

# replacing

name = "Lia Javanshir"
name = name.replace("Lia", "javanshir")
name = name.replace("javanshir", "Lia")
print(name)

#done