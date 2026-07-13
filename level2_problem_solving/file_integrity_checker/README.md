# File Integrity Checker

## Overview

The File Integrity Checker is a Python application that monitors the integrity of files in a selected directory by generating SHA256 hashes. It creates a baseline of file hashes and compares them with the current hashes to detect modified, missing, or newly added files.

## Objectives

- Learn file integrity verification using hashing.
- Generate SHA256 hashes for files.
- Store baseline hashes in a JSON file.
- Compare current file hashes with the baseline.
- Detect modified, missing, and new files.

## Features

- Create a baseline of file hashes.
- Verify file integrity against the baseline.
- Detect modified files.
- Detect missing files.
- Detect newly added files.
- Exception handling for unreadable files.

## Technologies Used

- Python 3
- os Module
- json Module
- hashlib Module

## Project Files

```
file_integrity_checker/
│── file_integrity_checker.py
│── baseline.json
│── README.md
```

## How to Run

```bash
python file_integrity_checker.py
```

## Program Menu

```
=========FILE INTEGRITY CHECKER=========

1. Create Baseline
2. Verify Baseline
3. Exit
```

## Sample Output

### Create Baseline

```
=========FILE INTEGRITY CHECKER=========

1. Create Baseline
2. Verify Baseline
3. Exit

Enter your choice: 1

Enter the folder path to create baseline:
C:\Users\Aamina\Desktop\Test

Baseline created successfully.
```

---

### Verify Baseline

```
Enter your choice: 2

Enter folder_path:
C:\Users\Aamina\Desktop\Test
```

If no changes are detected:

```
document.txt is unchanged.
photo.jpg is unchanged.
notes.pdf is unchanged.
```

---

If a file has been modified:

```
document.txt has been modified.
```

---

If a file is missing:

```
photo.jpg is missing.
```

---

If a new file is detected:

```
New file detected: report.docx
```

---

If a file cannot be read:

```
Couldn't read document.txt: Permission denied
```

---

### Exit

```
Enter your choice: 3

Thank you for using the File Integrity Checker.
Exiting the program.
```

## Learning Outcomes

Through this project, the following concepts were implemented:

- Functions
- Loops
- Dictionaries
- File Handling
- JSON Handling
- SHA256 Hashing
- Exception Handling
- os.listdir()
- os.path.join()
- hashlib.sha256()
