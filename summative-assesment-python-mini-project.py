# Function to calculate the letter grade
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Function to print student summary
def print_summary(student_list):
    print("\nStudent Summary:")
    for student in student_list:
        name, score, grade = student
        print(f"{name}: {score} -> {grade}")

# Function to save student data to a file
def save_to_file(student_list):
    with open("grades.txt", "w") as file:
        for student in student_list:
            name, score, grade = student
            file.write(f"{name}: {score} -> {grade}\n")

# Main Program
print("Welcome to the Student Grade Tracker!")
students = []

while True:
    name = input("\nEnter student name: ").strip().title()
    try:
        score = float(input("Enter score (0–100): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    grade = get_letter_grade(score)
    students.append((name, score, grade))

    again = input("\nAdd another student? (yes/no): ").strip().lower()
    if again != 'yes':
        break

print_summary(students)
save_to_file(students)
print("\nStudent data saved to grades.txt")
