# Fixed-Length Course Management System

## Overview
This Python program manages a list of courses using fixed-length records. It allows the user to add, search, delete, list, and edit courses. The courses are stored in a text file named `FixedLengthRecords.txt`.

## Key Components
- **Course Class:** Represents a course with attributes like code, title, type, credit hours, and semester. It ensures that the code and title are of fixed lengths (8 and 40 characters, respectively).
- **File Operations:** Courses are stored in a file called `FixedLengthRecords.txt`. The program reads from and writes to this file based on user actions.
- **Padding Function:** Ensures that the string representation of each attribute meets the required fixed length.

## Features
- **Add a Course:** Allows the user to add a new course.
- **Search for a Course:** Allows the user to search for a course by its code.
- **Delete a Course:** Allows the user to delete a course by its code.
- **List All Courses:** Lists all the courses in the file.
- **Edit a Course:** Allows the user to edit a course by its code.

## How to Run
1. Save the provided code in a file, for example, `FixedLengthRecord.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where `FixedLengthRecord.py` is saved.
4. Run the following command:

```sh
FixedLengthRecord.py
```

## User Menu
- **a) Add:** Add a new course.
- **s) Search:** Search for a course by code.
- **d) Delete:** Delete a course by code.
- **l) List All:** List all courses.
- **e) Edit:** Edit a course by code.
- **q) Quit:** Exit the program.

## Example Usage

Upon running the program, you will be prompted to enter your choice based on the menu options. Follow the prompts to interact with the fixed-length course management system.
