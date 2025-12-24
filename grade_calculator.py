def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work!"
    elif marks >= 80:
        return "B", "Good work, keep it up!"
    elif marks >= 70:
        return "C", "Good effort, you can do better."
    elif marks >= 60:
        return "D", "Needs improvement, don't give up."
    else:
        return "F", "Keep trying, success takes practice."

while True:
    name = input("Enter student name: ")
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100. ")
    except ValueError:
        print("Invalid input. Please enter numeric marks")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
    