# Unit 4: Programming Assignment – Recursive Functions

This repository contains the recursive functions implementation developed as part of Unit 4 for the Programming course (Q2-2026).

The primary objective of this assignment is to understand how recursive algorithms work by implementing several classic recursive functions in Python while incorporating proper error handling techniques to prevent crashes caused by invalid input.

## Project Description

### Recursive Functions Implementation

The objective of this assignment is to implement and analyze several recursive functions commonly used to solve mathematical and algorithmic problems. Each function demonstrates the use of a **base case** and a **recursive case**, allowing the problem to be solved by repeatedly reducing it until the stopping condition is reached.

To improve the robustness of the program, all functions include input validation and exception handling using `try/except`, preventing runtime errors such as infinite recursion, invalid data types, division by zero, and other invalid inputs described in the tutorial.

The project also includes the corresponding pseudocode (PPP) and a flowchart representing the logic of each recursive function before implementation.

This assignment demonstrates the importance of recursive problem solving, algorithm design, input validation, and defensive programming practices.

---

## Repository Structure

All deliverables for this assignment are located inside the official folder:

**Classwork-16-Recursive-Functions/**

### Contents

* **recursive_functions.py** — Python program implementing all recursive functions from the tutorial, including complete input validation, exception handling using `try/except`, and professional structural comments.
* **recursive_functions_ppp.txt** — Pseudocode Programming Process (PPP) describing the logic of each recursive function before implementation.
* **recursive_functions_flowchart.png** — Flowchart representing the recursive logic based on the corresponding pseudocode.

---

## Implementation Details & Architecture

### 1. Countdown Recursion (`recursiva`)

Implements a simple recursive countdown that repeatedly decreases the input value until reaching the base case.

### 2. Fibonacci (`fibonacci`)

Calculates the nth Fibonacci number using recursive calls based on the two previous values in the sequence.

### 3. Factorial (`factorial`)

Computes the factorial of a non-negative integer through recursive multiplication.

### 4. Recursive Multiplication (`multiplicacion_recursiva`)

Performs multiplication using only recursive addition instead of the multiplication operator.

### 5. Recursive Integer Division (`division_entera_recursiva`)

Calculates integer division by repeatedly subtracting the divisor until the dividend becomes smaller.

### 6. Recursive Power (`potencia_recursiva`)

Calculates the power of a number by recursively multiplying the base until the exponent reaches zero.

### 7. Collatz Sequence (`serie_collatz`)

Generates the Collatz sequence recursively until the value reaches the stopping condition.

### 8. Flatten JSON (`aplanar_json`)

Traverses nested dictionaries recursively and converts them into a single-level dictionary using compound keys.

### 9. Error Handling

All recursive functions validate their inputs before making recursive calls. Invalid values such as negative numbers, incorrect data types, division by zero, or unsupported structures are handled using `try/except`, allowing the program to continue executing without crashing.

### 10. Program Organization

The program is divided into eight functions:

* `recursiva`
* `fibonacci`
* `factorial`
* `multiplicacion_recursiva`
* `division_entera_recursiva`
* `potencia_recursiva`
* `serie_collatz`
* `aplanar_json`

This modular organization improves readability, maintainability, and code reuse while making each recursive algorithm independent and easier to understand.

---

## Environment and Tools

* **Language:** Python
* **Version Control:** Git
* **Hosting & Collaboration Platform:** GitHub

---

## AI Use Declaration

AI tools were used to assist in reviewing the recursive function implementations, improving code organization, verifying proper recursive logic, and incorporating appropriate exception handling for invalid inputs. AI was also consulted to help prepare the project documentation, pseudocode, and flowchart while preserving the intended behavior, learning objectives, and recursive implementation required for the assignment.
