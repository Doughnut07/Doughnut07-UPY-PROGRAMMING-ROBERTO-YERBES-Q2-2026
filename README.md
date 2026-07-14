# Unit 3: Programming Assignment – Error Handling

This repository contains the error handling implementation developed as part of Unit 3 for the Programming course (Q2-2026).

The primary objective of this assignment is to improve the robustness of the programs developed in previous classworks by incorporating proper exception handling techniques. The updated programs are able to detect and manage common runtime errors, preventing unexpected crashes while providing meaningful feedback to the user.

---

# Project Description

## Error Handling Implementation

The objective of this assignment is to enhance the reliability of the previously developed applications by integrating structured error handling.

The programs were updated using Python's `try`, `except`, and related exception handling mechanisms to safely manage situations such as invalid user input, missing files, file access errors, and unexpected runtime exceptions.

Instead of terminating abruptly when an error occurs, each application now displays an informative message and continues or exits gracefully depending on the situation.

This assignment demonstrates one of the most important software engineering practices: writing programs that can anticipate errors and respond to them in a controlled and user-friendly manner.

---

# Repository Structure

All deliverables for this assignment are located inside the official folder:

`Classwork-14-Error-Handling/`

Contents:

- `school management system.py` — Updated version of the School Management System including professional structural comments (`# INPUT`, `# PROCESS`, and `# OUTPUT`) and exception handling.
- `mandelbrot set math.py` — Updated Mandelbrot Set generator with error handling for configuration loading, file operations, and data processing.
- `mandelbrot set vis.py` — Updated Mandelbrot visualization program including exception handling while reading CSV files, generating the image, and saving the final output.

---

# Implementation Details & Architecture

## 1. Input Validation

Each program validates user input before processing it.

Whenever invalid information is entered, the application catches the corresponding exception and informs the user instead of terminating unexpectedly.

---

## 2. File Handling Protection (PROCESS)

Programs that read external files now verify that the required files exist and can be accessed correctly.

Common file-related exceptions such as missing configuration files or inaccessible CSV files are handled using appropriate exception blocks.

---

## 3. Runtime Exception Handling

Operations that may produce runtime errors are enclosed within `try` blocks.

Specific exceptions are handled individually whenever possible, while unexpected exceptions are managed through a general exception handler that prevents the application from crashing.

---

## 4. Program Continuity (OUTPUT)

Whenever possible, the applications continue executing after handling recoverable errors.

If execution cannot safely continue, the programs terminate gracefully while displaying a descriptive error message explaining what happened.

---

# Environment and Tools

- Language: Python
- External Library: Pillow (PIL) *(used by the Mandelbrot Visualization program)*
- Version Control: Git
- Hosting & Collaboration Platform: GitHub

---

# AI Use Declaration

AI tools were used to assist in reviewing the exception handling implementation, improving code organization, and preparing the project documentation. AI was also consulted to verify that appropriate error handling techniques were applied consistently across the School Management System, the Mandelbrot Set generator, and the Mandelbrot Visualization programs while maintaining the original functionality of each application.