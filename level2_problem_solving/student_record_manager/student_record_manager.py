def display_records():
    file=open("students.txt")
    contents=file.read()
    if contents=="":
        print("No student records found.")
    else:
        print(contents)
    file.close()

def add_student():
    file=open("students.txt","r")
    records=file.readlines()
    usn=input("Enter student usn:")
    duplicate=False
    for record in records:
        record=record.strip().split(",")
        if usn==record[0]:
            duplicate=True
            print("USN already exists.")
            break
    if not duplicate:
        name=input("Enter student name:")
        age=input("Enter student age:")
        programme=input("Enter student programme:")
        cgpa=input("Enter student cgpa:")
        file=open("students.txt","a")
        file.write(f"{usn},{name},{age},{programme},{cgpa}\n\n")
        print("Credentials Saved!")
    file.close()

def search_student():
    file=open("students.txt")
    records=file.readlines()
    usn=input("Enter student USN:")
    found=False
    for record in records:
        record=record.strip().split(",")
        if usn==record[0]:
            found=True
            print("Student found.")
            print(f"USN: {record[0]}\nName: {record[1]}\nAge: {record[2]}\nProgramme: {record[3]}\nCGPA: {record[4]}\n")
            break
    if not found:
            print("Student not found. Try again.")
    file.close()
    return


def update_student():
    file = open("students.txt", "r")
    records = file.readlines()
    file.close()
    usn = input("Enter student USN: ")
    updated_records = []
    found = False
    for record in records:
        record = record.strip().split(",")
        if usn == record[0]:
            found = True
            print("Choose what you want to update")
            choice = int(input("1.USN\n2.Name\n3.Age\n4.Programme\n5.CGPA\n"))
            if choice == 1:
                record[0] = input("Enter new USN: ")
            elif choice == 2:
                record[1] = input("Enter new Name: ")
            elif choice == 3:
                record[2] = input("Enter new Age: ")
            elif choice == 4:
                record[3] = input("Enter new Programme: ")
            elif choice == 5:
                record[4] = input("Enter new CGPA: ")
            else:
                print("Invalid choice.")
                return
            print("Record updated successfully.")
        new_line = ",".join(record)
        updated_records.append(new_line + "\n")
    if not found:
        print("Student not found.")
        return
    file = open("students.txt", "w")
    file.writelines(updated_records)
    file.close()

def delete_student():
    file=open("students.txt","r")
    records = file.readlines()
    file.close()
    deleted_records = []
    usn=input("Please enter the USN of the student you want to delete:")
    found = False
    for record in records:
        record = record.strip().split(",")
        if usn == record[0]:
            found = True
            surity=input("Are you sure you want to delete this?(y/n): ")
            if surity.lower()=="y":
                print("Record Deleted")
                continue
        new_line = ",".join(record)
        deleted_records.append(new_line + "\n")
    if not found:
        print("No student found.")
        return
    file=open("students.txt","w")
    file.writelines(deleted_records)
    file.close()
    return

print("======== STUDENT RECORD MANAGER ========")
print("Select an option:")
choice=input("1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5.Delete Student\n6. EXIT\n")
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
    print("Thank you for using our service.")
else:
    print("Invalid choice. Please try again.")
    exit()