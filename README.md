# Unit 3: Programming Assignment – School Management System

This repository contains a Python-based implementation developed as part of Unit 3 for the Programming course (Q2-2026).

The primary objective of this assignment is to design and build a role-based school management system using structured programming, applying clean code practices, dictionary data structures, and conditional logic to simulate a real-world authentication and grade management workflow.

---

## Project Description

### School Management System

The main objective of this application is to simulate a basic school management platform where different users — **students**, **professors**, and a **coordinator** — log in with their credentials and are presented with a personalized interface based on their role.

Since real-world systems require access control and role differentiation, this program uses a dictionary-based user database to authenticate users and dynamically display relevant information and options depending on who is logged in.

---

## Repository Structure

All deliverables for this assignment are located inside the official folder: `Classwork-10-School-Management-System/`

- `school_management_system.py` — The working Python program organized with professional structural comments (`# INPUT`, `# PROCESS`, and `# OUTPUT`).
- `PPP.txt` — The complete and structured pseudocode following strict class rules (Plain English, `←` for assignments, `#` for comments, and zero Python syntax).
- `Flowchart.png` — The exported flowchart diagram covering the login loop logic, role-based decision flow, and the grade modification workflow for the professor mode.

---

## Implementation Details & Architecture

### 1. Data Structures & Input Definition

- **User Dictionary:** All users (students, professors, and the coordinator) are stored in a nested dictionary containing their password, role, and full name.
- **Subjects Tuple:** The list of academic subjects is stored as an immutable tuple, ensuring the course catalog cannot be accidentally modified during execution.
- **Grades Dictionary:** Each student's grades are stored in a nested dictionary indexed by username and subject name, allowing direct and efficient lookups.

### 2. Authentication Loop (PROCESS)

A `while` loop continuously prompts the user for a username and password until a successful match is found:

- If the username does not exist in the system, an error message is displayed.
- If the username exists but the password is incorrect, a specific warning is shown.
- Once both fields match, the loop exits and the session is established with the authenticated user's role.

### 3. Role-Based Output (OUTPUT)

Upon successful login, the program branches into one of three modes based on the authenticated user's role:

- **Student:** Displays a full personal report card with all subject grades. Each subject is automatically classified into a passed set (grade ≥ 7.0) or a pending set (grade < 7.0) using Python set structures.
- **Professor:** Lists all enrolled students and allows the professor to select a student and a subject to update their grade. Includes input validation, an exit keyword at every step, and a yes/no confirmation before applying any change.
- **Coordinator:** Displays a complete overview of the system — the full teacher list, the subject catalog, and every student's grades across all subjects.

---

## Environment and Tools

- **Language:** Python
- **Version Control:** Git
- **Hosting & Collaboration Platform:** GitHub

---

## AI Use Declaration

AI tools were used to assist in designing and exporting the **Flowchart.png**, helping translate the program's logic into a clear visual diagram. AI was also consulted for **support during the development of certain sections** of `school_management_system.py`, specifically for structuring the role-based conditional blocks and set operations. 