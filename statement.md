# Project Statement: Student Grade Management System

## Problem Statement
Managing student grades, subjects, and registration details via spreadsheets or heavy enterprise software is often overkill for lightweight use cases—such as individual tutors, small coaching modules, or rapid CLI administration.

---

## Scope of the Project
* *In-Scope*:
  * In-memory CRUD operations (Add, Update, Delete, View) mapped by unique registration numbers.
  * Capturing core attributes: Registration Number, Name, Grade, and Subject.
  * Modular code separation (Grade.py logic vs. CLI runner loop).
  * Interactive terminal menu with basic choice validation.
* *Out-of-Scope*:
  * Persistent storage (database, JSON, or CSV file saving/loading).
  * Multi-subject transcripts per registration ID (current model overwrites/stores a single flat record per registration key).
  * User authentication, authorization, or multi-user roles.
  * Statistical aggregation (class averages, GPA calculations, CSV/PDF report generation).

---

## Target Users
* *Individual Tutors*: Quick lightweight tracking for private students.
* *Small Workshop / Class Coordinators*: Minimalist terminal tool for tracking participant check-ins/grades.
* *Python Learners & Educators*: Clean baseline reference for dictionary-based CRUD patterns and modular imports (from Grade import ...).

---

## High-Level Features
1. *Add Student (add_student)*: Inserts a new student record into the in-memory dictionary keyed by registration_number.
2. *Update Student (update_student)*: Validates existence and overwrites attributes for a given registration number.
3. *Delete Student (delete_student)*: Removes target records safely with existence checks.
4. *View Students (view_students)*: Iterates and prints formatted tabular/inline summaries of all active records.
5. *Interactive CLI Runner (main)*: Continuous while True loop providing menu-driven navigation and feedback loops.