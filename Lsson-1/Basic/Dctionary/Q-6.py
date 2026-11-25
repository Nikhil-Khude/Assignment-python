student = {
    "name": "Nikhil",
    "age": 22,
    "course": "MCA"
}

new_student=student.copy()
new_student.update({"course":"Python"})
new_student["City"]="Pune"
print(student)
print(new_student)