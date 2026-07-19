# Student Record Manager

## Overview

The Student Record Manager is a Python-based command-line application that allows users to manage student records efficiently. The application stores data in a JSON file, allowing records to persist even after the program is closed. It provides features to add, view, search, update, delete, sort, filter, and export student records.

---

## Features

- Add new student records.
- Prevent duplicate USNs.
- View all student records.
- Filter student records by Programme.
- Filter student records by CGPA range.
- Search for a student using their USN.
- Update student details.
- Delete student records with confirmation.
- Sort student records by Name.
- Sort student records by CGPA (Ascending or Descending).
- Display the Top 5 students based on CGPA.
- Export all student records to a CSV file.

---

## Technologies Used

- Python 3
- JSON
- CSV Module

---

## File Structure

```
Student_Record_Manager/
│
├── student_record_manager.py
├── students.json
├── students.csv
└── README.md
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the following command:

```bash
python student_record_manager.py
```

---

## Main Menu

```
======== STUDENT RECORD MANAGER ========

Select an option:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Sort Student
7. Export to CSV
8. EXIT
```

---

# Functionalities

## 1. Add Student

Adds a new student record to the JSON database while ensuring that every student has a unique USN.

---

## 2. View Students

Displays all student records or allows filtering by Programme or CGPA range.

---

## 3. Search Student

Searches for a student using their USN and displays the student's details if found.

---

## 4. Update Student

Updates a selected field of an existing student record.

Available fields:

- USN
- Name
- Age
- Programme
- CGPA

---

## 5. Delete Student

Deletes a student record after confirmation.

---

## 6. Sort Student

Allows users to:

- Sort students alphabetically by Name.
- Sort students by CGPA in Ascending Order.
- Sort students by CGPA in Descending Order.
- Display the Top 5 students based on CGPA.

---

## 7. Export to CSV

Exports all student records from the JSON database into a CSV file.

---

## Data Storage

Student records are stored in a JSON file named `students.json`.

Example:

```json
[
    {
        "usn": "4NM23CS001",
        "name": "Aamina",
        "age": "19",
        "programme": "Cybersecurity",
        "cgpa": "9.60"
    }
]
```

---

## CSV Output

The exported CSV file contains the following columns:

```
USN,Name,Age,Programme,CGPA
```

---
# Sample Outputs

---

## 1. Add Student

### Add Student Successfully

```
Enter student usn: 4NM23CS001
Enter student name: Aamina
Enter student age: 19
Enter student programme: Cybersecurity
Enter student cgpa: 9.60

Credentials Saved!
```

### Duplicate USN

```
Enter student usn: 4NM23CS001

USN already exists.
```

---

## 2. View Students

### View All Records

```
Choose how you want to view records:

1. View ALL records
2. View by FILTERING

Enter choice: 1

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

USN: 4NM23CS002
Name: Rahul
Age: 20
Programme: Computer Science
CGPA: 8.72
```

---

### No Student Records

```
Choose how you want to view records:

1. View ALL records
2. View by FILTERING

Enter choice: 1

No student records found.
```

---

## View by Filtering

```
Choose how you want to view records:

1. View ALL records
2. View by FILTERING

Enter choice: 2

Select a filter:

1. By Programme
2. By CGPA range
```

---

### Filter by Programme

```
Enter a programme name from the following:

Data Science
AI Development
Computer Science
Cybersecurity
Artificial Intelligence
Information Science

Cybersecurity

FILTER APPLIED: PROGRAMME

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

USN: 4NM23CS007
Name: Sarah
Age: 20
Programme: Cybersecurity
CGPA: 9.12
```

---

### Invalid Programme

```
Enter a programme name from the following:

Data Science
AI Development
Computer Science
Cybersecurity
Artificial Intelligence
Information Science

Mechanical

Enter a valid program name and try again.
```

---

### No Students Found in Programme

```
Enter a programme name from the following:

Data Science
AI Development
Computer Science
Cybersecurity
Artificial Intelligence
Information Science

Information Science

FILTER APPLIED: PROGRAMME

No students found in this programme.
```

---

### Filter by CGPA Range

```
Enter minimum CGPA: 8.5
Enter maximum CGPA: 9.5

FILTER APPLIED: CGPA RANGE

USN: 4NM23CS002
Name: Rahul
Age: 20
Programme: Computer Science
CGPA: 8.72

USN: 4NM23CS007
Name: Sarah
Age: 20
Programme: Cybersecurity
CGPA: 9.12
```

---

### No Students Found in CGPA Range

```
Enter minimum CGPA: 9.95
Enter maximum CGPA: 10

FILTER APPLIED: CGPA RANGE

No students found in this CGPA range.
```

---

## 3. Search Student

### Student Found

```
Enter student USN: 4NM23CS001

Student found.

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60
```

---

### Student Not Found

```
Enter student USN: 4NM23CS999

Student not found. Try again.
```
---

## 4. Update Student

### Update USN

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA

Enter choice: 1

Enter new USN: 4NM23CS101

Record updated successfully.
```

---

### Update Name

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA

Enter choice: 2

Enter new Name: Aamina Sheikh

Record updated successfully.
```

---

### Update Age

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA

Enter choice: 3

Enter new Age: 20

Record updated successfully.
```

---

### Update Programme

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA

Enter choice: 4

Enter new Programme: Artificial Intelligence

Record updated successfully.
```

---

### Update CGPA

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA

Enter choice: 5

Enter new CGPA: 9.80

Record updated successfully.
```

---

### Student Not Found

```
Enter student USN: 4NM23CS999

Student not found.
```

---

### Invalid Update Choice

```
Enter student USN: 4NM23CS001

Choose what you want to update

1.USN
2.Name
3.Age
4.Programme
5.CGPA

Enter choice: 9

Invalid choice.
```

---

## 5. Delete Student

### Delete Successfully

```
Please enter the USN of the student you want to delete:

4NM23CS001

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

Are you sure you want to delete this?(y/n): y

Record Deleted
```

---

### Delete Cancelled

```
Please enter the USN of the student you want to delete:

4NM23CS001

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

Are you sure you want to delete this?(y/n): n

Deletion cancelled.
```

---

### Student Not Found

```
Please enter the USN of the student you want to delete:

4NM23CS999

No student found.
```

---

## 6. Sort Student

### Sort by Name

```
Choose how you want to sort the students:

1. By NAME
2. By CGPA

Enter choice: 1

SORTING BY NAME....

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

USN: 4NM23CS004
Name: Rahul
Age: 20
Programme: Computer Science
CGPA: 8.75

USN: 4NM23CS003
Name: Sarah
Age: 19
Programme: AI Development
CGPA: 9.15
```

---

### Sort by CGPA (Ascending)

```
Choose how you want to sort the students:

1. By NAME
2. By CGPA

Enter choice: 2

Choose the order of sorting:

1. Ascending Order
2. Descending Order
3. Display the first 5 students

Enter choice: 1

SORTING BY CGPA in ASCENDING ORDER....

USN: 4NM23CS004
Name: Rahul
Age: 20
Programme: Computer Science
CGPA: 8.75

USN: 4NM23CS003
Name: Sarah
Age: 19
Programme: AI Development
CGPA: 9.15

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60
```

---

### Sort by CGPA (Descending)

```
Choose how you want to sort the students:

1. By NAME
2. By CGPA

Enter choice: 2

Choose the order of sorting:

1. Ascending Order
2. Descending Order
3. Display the first 5 students

Enter choice: 2

SORTING BY CGPA in DESCENDING ORDER....

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

USN: 4NM23CS003
Name: Sarah
Age: 19
Programme: AI Development
CGPA: 9.15

USN: 4NM23CS004
Name: Rahul
Age: 20
Programme: Computer Science
CGPA: 8.75
```

---

### Display Top 5 Students

```
Choose how you want to sort the students:

1. By NAME
2. By CGPA

Enter choice: 2

Choose the order of sorting:

1. Ascending Order
2. Descending Order
3. Display the first 5 students

Enter choice: 3

DISPLAYING THE TOP 5 STUDENTS....

USN: 4NM23CS001
Name: Aamina
Age: 19
Programme: Cybersecurity
CGPA: 9.60

USN: 4NM23CS003
Name: Sarah
Age: 19
Programme: AI Development
CGPA: 9.15

USN: 4NM23CS005
Name: Arjun
Age: 20
Programme: Data Science
CGPA: 9.03

USN: 4NM23CS006
Name: Neha
Age: 19
Programme: Information Science
CGPA: 8.92

USN: 4NM23CS004
Name: Rahul
Age: 20
Programme: Computer Science
CGPA: 8.75
```

---

### Invalid Sort Choice

```
Choose how you want to sort the students:

1. By NAME
2. By CGPA

Enter choice: 5

Please enter the number 1 or the number 2 and try again.
```

---

### Invalid Sorting Order

```
Choose the order of sorting:

1. Ascending Order
2. Descending Order
3. Display the first 5 students

Enter choice: 7

Please enter the number 1, 2, or 3 and try again.
```

---

## 7. Export to CSV

### Export Student Records

```
Exported Student Records Successfully.
```

The generated `students.csv` file:

| USN | Name | Age | Programme | CGPA |
|-----|------|-----|-----------|------|
| 4NM23CS001 | Aamina | 19 | Cybersecurity | 9.60 |
| 4NM23CS002 | Rahul | 20 | Computer Science | 8.75 |
| 4NM23CS003 | Sarah | 19 | AI Development | 9.15 |

---

## 8. Exit

```
Thank you for using our service.
```

---

## Invalid Main Menu Choice

```
======== STUDENT RECORD MANAGER ========

Select an option:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Sort Student
7. Export to CSV
8. EXIT

Enter choice: 10

Invalid choice. Please choose a number between 1 to 8 and try again.
```

---

# Conclusion

The Student Record Manager provides a simple and efficient way to manage student records using Python. It demonstrates the implementation of file handling, JSON data storage, searching, updating, deleting, sorting, filtering, and exporting records to CSV using a command-line interface.

This project helped strengthen core Python programming concepts, including functions, loops, conditional statements, file handling, lists, dictionaries, sorting, and data persistence.

---
