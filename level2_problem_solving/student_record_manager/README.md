# Student Record Manager

## Overview

The Student Record Manager is a menu driven Python application developed to perform basic CRUD (Create, Read, Update and Delete) operations on student records. The project demonstrates file handling using both text files and JSON files while maintaining student information efficiently.

## Objectives

- Implement file handling in Python.
- Perform CRUD operations on student records.
- Store and retrieve data using both text and JSON formats.
- Validate duplicate USNs before adding new records.
- Provide a simple menu driven interface for users.

## Features

- Add a new student
- Display all student records
- Search a student using USN
- Update student details
- Delete a student record with confirmation
- Supports both Text (.txt) and JSON (.json) storage

## Technologies Used

- Python 3
- File Handling
- JSON Module

## Project Files

```
student_record_manager/
│── student_record_manager.py
│── student_record_manager_json.py
│── students.txt
│── students.json
│── README.md
```

## Data Format

### Text File

```
USN,Name,Age,Programme,CGPA
```

Example:

```
4NM23CS001,Aarav Sharma,18,Computer Science,8.7
```

### JSON File

```json
{
    "usn": "4NM23CS001",
    "name": "Aarav Sharma",
    "age": 18,
    "programme": "Computer Science",
    "cgpa": 8.7
}
```

## Program Menu

```
======== STUDENT RECORD MANAGER ========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

## How to Run

### Text File Version

```bash
python student_record_manager.py
```

### JSON Version

```bash
python student_record_manager_json.py
```

## Sample Operations

### Add Student

- Enter USN
- Enter Name
- Enter Age
- Enter Programme
- Enter CGPA

### Search Student

Enter the student's USN to retrieve their details.

### Update Student

Search a student using USN and update any one of the following:

- USN
- Name
- Age
- Programme
- CGPA

### Delete Student

Search using USN and confirm deletion before removing the record.

## Learning Outcomes

Through this project, the following concepts were implemented:

- Functions
- Conditional statements
- Loops
- Lists
- Dictionaries
- File Handling
- JSON Handling
- CRUD Operations
- Data Validation
- User Input Handling

## Sample Output

### Main Menu

```
======== STUDENT RECORD MANAGER ========

Select an option:
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. EXIT
```

---

### Add Student

Input

```
Enter student USN: 4NM23CS021
Enter student name: John
Enter student age: 20
Enter student programme: CSE
Enter student cgpa: 8.9
```

Output

```
Credentials Saved!
```

If the USN already exists:

```
USN already exists.
```

---

### View Students

Output

```
USN: 4NM23CS001
Name: Aarav Sharma
Age: 18
Programme: Computer Science
CGPA: 8.7

USN: 4NM23CS002
Name: Ananya Rao
Age: 19
Programme: Computer Science
CGPA: 9.1
```

If there are no records:

```
No student records found.
```

---

### Search Student

Input

```
Enter student USN: 4NM23CS001
```

Output

```
Student found.

USN: 4NM23CS001
Name: Aarav Sharma
Age: 18
Programme: Computer Science
CGPA: 8.7
```

If not found:

```
Student not found. Try again.
```

---

### Update Student

Input

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA
```

Output

```
Record updated successfully.
```

If an invalid option is entered:

```
Invalid choice.
```

If the USN is not found:

```
Student not found.
```

---

### Delete Student

Input

```
Please enter the USN of the student you want to delete:
4NM23CS001

Are you sure you want to delete this? (y/n): y
```

Output

```
Record Deleted
```

If the user selects **n**:

```
Deletion cancelled.
```

If the USN does not exist:

```
No student found.
```

---

### Exit

```
Thank you for using our service.
```
