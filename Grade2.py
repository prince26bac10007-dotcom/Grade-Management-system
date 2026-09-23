#Grade.py
from Grade import add_student, update_student, delete_student, view_students

def main(): 
    while True: 
        print("\nStudent Grade Management System") 
        print("1. Add Student") 
        print("2. Update Student") 
        print("3. Delete Student") 
        print("4. View Students") 
        print("5. Exit") 
        
        choice = input("Enter your choice: ")

        if choice == '1': 
        

     

            registration_number = input("Enter student registration number: ") 
            name = input("Enter student name: ") 
            grade = int(input("Enter student grade: ")) 
            subject = input("Enter student subject: ") 
            add_student(registration_number, name, grade, subject) 
        elif choice == '2': 
            registration_number = input("Enter student registration number to update: ") 
            name = input("Enter new name: ") 
            grade = int(input("Enter new grade: ")) 
            subject = input("Enter new subject: ") 
            update_student(registration_number, name, grade, subject) 
        elif choice == '3': 
            registration_number = input("Enter student registration number to delete: ") 
            delete_student(registration_number) 
        elif choice == '4': 
            view_students() 
        elif choice == '5': 
            print("Exiting the program.") 
            break 
        else: 
            print("Invalid choice. Please try again.")

# This triggers the program to actually start running!
if __name__ == "__main__":
    main()