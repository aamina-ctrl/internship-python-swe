import json
def display_records():
    choice=int(input("Choose how you want to view records:\n1. View ALL records\n2. View by FILTERING\n"))
    if choice==1:
        file=open("students.json","r")
        students=json.load(file)
        if len(students)==0:
            print("No student records found.")
        else:
            for student in students:
                print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
        file.close()
    elif choice==2:
        choice2=int(input("Select a filter:\n1. By Programme\n2. By CGPA range"))
        if choice2==1:
            programme=input("Enter a programme name from the following:\nData Science\nAI Development\nComputer Science\nCybersecurity\nArtificial Intelligence\nInformation Science\n")
            if programme=="Data Science" or programme=="AI Development" or programme=="Computer Science" or programme=="Cybersecurity" or programme=="Artificial Intelligence" or programme=="Information Science":
                print("1 FILTER APPLIED: PROGRAMME")
                file=open("students.json","r")
                students=json.load(file)
                file.close()
            else:
                print("Enter a valid program name and try again.")
                

def add_student():
    file=open("students.json","r")
    students=json.load(file)
    file.close()
    usn=input("Enter student usn:")
    duplicate=False
    for student in students:
        if usn==student['usn']:
            duplicate=True
            print("USN already exists.")
            break
    if not duplicate:
        name=input("Enter student name:")
        age=input("Enter student age:")
        programme=input("Enter student programme:")
        cgpa=input("Enter student cgpa:")
        new_student={
            "usn": usn,
            "name": name,
            "age": age,
            "programme": programme,
            "cgpa": cgpa
        }
        students.append(new_student)
        file=open("students.json","w")
        json.dump(students,file)
        print("Credentials Saved!")
    file.close()

def search_student():
    file=open("students.json","r")
    students=json.load(file)
    usn=input("Enter student USN:")
    found=False
    for student in students:
        if usn==student['usn']:
            found=True
            print("Student found.")
            print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
            break
    if not found:
            print("Student not found. Try again.")
    file.close()
    return


def update_student():
    file = open("students.json", "r")
    students = json.load(file)
    file.close()
    usn = input("Enter student USN: ")
    found = False
    for student in students:
        if usn == student['usn']:
            found = True
            print("Choose what you want to update")
            choice = int(input("1.USN\n2.Name\n3.Age\n4.Programme\n5.CGPA\n"))
            if choice == 1:
                student['usn'] = input("Enter new USN: ")
            elif choice == 2:
                student['name'] = input("Enter new Name: ")
            elif choice == 3:
                student['age'] = input("Enter new Age: ")
            elif choice == 4:
                student['programme'] = input("Enter new Programme: ")
            elif choice == 5:
                student['cgpa'] = input("Enter new CGPA: ")
            else:
                print("Invalid choice.")
                return
            print("Record updated successfully.")
    if not found:
        print("Student not found.")
        return
    file = open("students.json", "w")
    json.dump(students, file)
    file.close()

def delete_student():
    file=open("students.json","r")
    students = json.load(file)
    file.close()
    usn=input("Please enter the USN of the student you want to delete:")
    found = False
    for student in students:
        if usn == student['usn']:
            found = True
            print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
            surity=input("Are you sure you want to delete this?(y/n): ")
            if surity.lower()=="y":
                print("Record Deleted")
                students.remove(student)
            else:
                print("Deletion cancelled.")
    if not found:
        print("No student found.")
        return
    file=open("students.json","w")
    json.dump(students, file)
    file.close()
    return

def sort_student():
    file=open("students.json","r")
    students=json.load(file)
    file.close()
    sort=(input("Choose how you want to sort the students:\n1. By NAME\n2. By CGPA\n"))
    if sort =="1":
        print("SORTING BY NAME....")
        students.sort(key=lambda student:student["name"].lower())
        for student in students:
            print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
    elif sort=="2":
        order=int(input("Choose the order of sorting:\n1. Ascending Order\n2. Descending Order\n3. Display the first 5 students\n"))
        if order==1:
            print("SORTING BY CGPA in ASCENDING ORDER....\n")
            students.sort(key=lambda student:(student["cgpa"]))
            for student in students:
                print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
        elif order==2:
            print("SORTING BY CGPA in DESCENDING ORDER....\n")
            students.sort(key=lambda student:(student["cgpa"]), reverse=True)
            for student in students:
                print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
        elif order==3:
            print("DISPLAYING THE TOP 5 STUUDENTS....\n")
            students.sort(key=lambda student:(student["cgpa"]), reverse=True)
            for i in range(5):
                student=students[i]
                print(f"USN: {student['usn']}\nName: {student['name']}\nAge: {student['age']}\nProgramme: {student['programme']}\nCGPA: {student['cgpa']}\n")
        else:
            print ("Please enter the number 1 or the number 2 and try again.")
    else:
        print ("Please enter the number 1 or the number 2 and try again.")

def export_csv():
    file=open("students.json","r")
    students=json.load(file)
    file.close()

    import csv
    file=open("students.csv","w",newline="")
    writer=csv.writer(file)
    writer.writerow(["USN","Name","Age","Programme","CGPA"])
    for student in students:
        writer.writerow([
            student["usn"],
            student["name"],
            student["age"],
            student["programme"],
            student["cgpa"],
        ])
    file.close()
    print("Exported Student Records Successfully.")

def statistics():
    pass


print("======== STUDENT RECORD MANAGER ========")
print("Select an option:")
choice=input("1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Sort Student\n7. Export to CSV\n8. Statistics\n9. EXIT\n")
if choice=="1":
    add_student()
elif choice=="2":
    display_records()
elif choice=="3":
    search_student()
elif choice=="4":
    update_student()
elif choice=="5":
    delete_student()
elif choice=="6":
    sort_student()
elif choice=="7":
    export_csv()
elif choice=="8":
    statistics()
elif choice=="9":
    print("Thank you for using our service.")
else:
    print("Invalid choice. Please choose a number between 1 to 8 and try again.")
    exit()