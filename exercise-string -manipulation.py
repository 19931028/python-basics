# 1. Split the string
to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

# 2. Split lyrics by line 
lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"""

changed_values = lyrics.splitlines()
print(changed_values)


long_village_name="Llanfairpwl1gwyngy11gogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM'
my_folders = my_path.strip().split("/")
print(my_folders)

#Given this list of names, change the third name in the list to be "Wolfgang Mozart".
composers = "Beethoven, Ludwig von; Liszt, Franz;Mozart,Wolfgang;Copland,Aaron"
composers = composers.replace('Mozart, Wolfgang', 'Wolfgang Mozart')
print(composers)

# Separate the composers
composers_split = composers.split(";")
print(composers_split)

# Get the third composer
third_composer = composers_split[2]
print(third_composer)

# Find the comma in the name
comma_position = third_composer.find(",")
print(comma_position)

# Join the names to get the 3rd composer's name in "first last" format
first_name = "Wolfgang"
last_name = "Mozart"
full_name = first_name  + " " + last_name
print(f"{first_name} {last_name}")
print(full_name)


# Clean right and left padded strings to get final message
left_padded = " Operators are standing by"
right_padded = "Call now "
combined = right_padded.rstrip() + '! ' + left_padded.lstrip()
print(combined)

#  Old-style string formatting with zero-padded assignment ID and percent
student_name = "Owen"
grade = 94.75
assignment_number = 12
formatted = "Student name: %s, Assignment ID: %04d, Grade: %.2f%%" % (student_name, assignment_number, grade)
print(formatted)


# Pad employee ID to 6 digits
employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print(employee_id_padded) 

# Print using raw strings
print(r"\n represents a new line.")


# Convert strings 
i_want_to_yell = "yeah"
I_NEED_TO_BE_QUIET = "SHHHHH"
this_is_a_title = "this is a title"
sWAPcASE = "sWAPcASE"
capitalize_this = "capitalize this"
print(i_want_to_yell.upper()) 
print(I_NEED_TO_BE_QUIET.lower()) 
print(this_is_a_title.title()) 
print(sWAPcASE.swapcase()) 
print(capitalize_this.capitalize()) 