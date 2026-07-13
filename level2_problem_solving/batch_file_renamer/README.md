# Batch File Renamer

## Overview

The Batch File Renamer is a Python application that renames multiple files in a selected directory using a user defined prefix while preserving the original file extensions. The program displays a preview of the new file names before renaming and asks for user confirmation.

## Objectives

- Learn file and directory handling using Python.
- Perform batch file renaming.
- Preserve original file extensions.
- Preview changes before renaming.
- Handle file renaming errors using exception handling.

## Features

- Display all files in a selected directory.
- Rename multiple files with a custom prefix.
- Automatically number renamed files.
- Preserve original file extensions.
- Preview old and new filenames.
- Confirmation before renaming.
- Error handling using try and except.

## Technologies Used

- Python 3
- os Module
- Exception Handling

## Project Files

```
batch_file_renamer/
│── batch_file_renamer.py
│── README.md
```

## How to Run

```bash
python batch_file_renamer.py
```

## Program Workflow

1. Enter the folder path.
2. Display all files in the folder.
3. Enter a prefix.
4. Preview the new filenames.
5. Confirm whether to proceed.
6. Rename all files while preserving their extensions.

## Sample Output

### Enter Folder Path

```
Enter the folder path:
C:\Users\Aamina\Desktop\Test
```

---

### Display Files

```
Files in the directory:

cat.jpg
dog.png
notes.txt
```

---

### Enter Prefix

```
Enter the prefix for the new file names:
holiday
```

---

### Preview Renaming

```
cat.jpg -> holiday_1.jpg
dog.png -> holiday_2.png
notes.txt -> holiday_3.txt
```

---

### Confirmation

```
Do you want to rename the files? (y/n):
```

If user enters:

```
y
```

Output

```
Renamed cat.jpg to holiday_1.jpg
Renaming completed successfully.

Renamed dog.png to holiday_2.png
Renaming completed successfully.

Renamed notes.txt to holiday_3.txt
Renaming completed successfully.
```

---

If user enters:

```
n
```

Output

```
Renaming cancelled.
```

---

### Error Handling

If a file cannot be renamed:

```
Error occurred while renaming file_name: <error_message>
Skipped renaming this file.
```

## Learning Outcomes

Through this project, the following concepts were implemented:

- Functions
- User Input
- Loops
- String Manipulation
- File and Directory Handling
- os Module
- os.listdir()
- os.path.splitext()
- os.path.join()
- os.rename()
- Exception Handling using try and except

## Sample Output

### Display Files

```
Enter the folder path:
C:\Users\Aamina\Desktop\Test

Files in the directory:
cat.jpg
dog.png
notes.txt
```

---

### Preview New File Names

```
Enter the prefix for the new file names:
holiday

cat.jpg -> holiday_1.jpg
dog.png -> holiday_2.png
notes.txt -> holiday_3.txt
```

---

### Confirmation

```
Do you want to rename the files? (y/n): y
```

---

### Successful Renaming

```
Renamed cat.jpg to holiday_1.jpg
Renaming completed successfully.

Renamed dog.png to holiday_2.png
Renaming completed successfully.

Renamed notes.txt to holiday_3.txt
Renaming completed successfully.
```

---

### If User Cancels

```
Do you want to rename the files? (y/n): n

Renaming cancelled.
```

---

### Error Handling

```
Error occurred while renaming cat.jpg: Permission denied
Skipped renaming this file.
```
