# Student Grade Management System

## Overview
The *Student Grade Management System*it helps administrators or educators to manage student academic records—including adding, updating, viewing, and deleting grades—using an in-memory dictionary storage model.

## Features
* Add Student: Register a new student with a unique registration number, full name, numeric grade, and subject.
* Update Student: Modify existing student attributes (name, grade, subject) referenced by registration number.
* Delete Student: Safely remove student records with validation checks for missing IDs.
* View Records: Output all stored student records cleanly formatted in the terminal.
* Interactive CLI Loop: Continuous menu-driven user experience until explicit exit.

## Technologies / Tools Used
* *Python 3.x: Core logic and runtime.
* *Python Standard Library*: In-memory dict data structures, standard I/O (input, print).
* *Terminal / CLI*: Cross-platform command-line execution interface.

## Suggested Project Structure
```text
student-grade-system/
│
├── Grade.py      # Core CRUD logic & global student dictionary
└── Grade2.py      # CLI interactive menu runner