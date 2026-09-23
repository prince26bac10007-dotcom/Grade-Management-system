student_grade = {} 

# Add new Student 
def add_student(registration_number, name, grade, subject): 
    student_grade[registration_number] = {'name': name, 'grade': grade, 'subject': subject} 
    print(f"Added {name} with a {grade} in {subject}") 

# Update a student 
def update_student(registration_number, name, grade, subject): 
    if registration_number in student_grade: 
        student_grade[registration_number] = {'name': name, 'grade': grade, 'subject': subject} 
        print(f"Student with registration number {registration_number} has been updated.") 
    else: 
        print(f"Student with registration number {registration_number} is not found") 

# Delete a student 
def delete_student(registration_number): 
    if registration_number in student_grade: 
        del student_grade[registration_number] 
        print(f"Student with registration number {registration_number} has been deleted.") 
    else: 
        print(f"Student with registration number {registration_number} is not found") 

# View the students 
def view_students(): 
    if student_grade: 
        for reg_num, info in student_grade.items(): 
            print(f"Registration Number: {reg_num}, Name: {info['name']}, Grade: {info['grade']}, Subject: {info['subject']}") 
    else: 
        print("No students found") 