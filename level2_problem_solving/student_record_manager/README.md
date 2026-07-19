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
