name = input("Enter student name: ")
usn = input("Enter USN: ")
age = input("Enter age: ")
gender = input("Enter gender: ")
phone = input("Enter contact number: ")
email = input("Enter email address: ")
course = input("Enter course: ")
semester = input("Enter semester: ")
address = input("Enter address: ")

print("\n--- STUDENT REGISTRATION SLIP ---")
print("Student Name     :", name)
print("USN              :", usn)
print("Age              :", age)
print("Gender           :", gender)
print("Contact Number   :", phone)
print("Email Address    :", email)
print("Course           :", course)
print("Semester         :", semester)
print("Address          :", address)

# Save to a file
with open("student_records.txt", "a") as f:
    f.write(f"{name}, {usn}, {age}, {gender}, {phone}, "
            f"{email}, {course}, {semester}, {address}\n")

print("\nStudent registered and details saved successfully!")