# Doughnut07-UPY-PROGRAMMING-ROBERTO-YERBES-Q2-2026´
Git/GitHub Repository

# Unit 2: Programming Assignment – Numerical Integration Calculator

This repository contains Python-based implementations developed as part of Unit 2 for the Programming course (Q2-2026). 

The primary objective of this assignment is to establish a professional software development environment using Git for version control and GitHub for remote collaboration, applying clean code practices and algorithmic optimization.

---

## Project Description

### Numerical Integration Calculator
The main objective of this application is to approximate the area under the curve of a mathematical function f(x) within a defined interval [a, b]. 

Since computers do not inherently integrate analytically (as one would do manually using calculus rules), this program uses geometric approximations. To achieve high precision, the program divides the total area into 1,000 small segments (n = 1000) and sums the area of each individual segment.

---

## Repository Structure

All deliverables for this assignment are located inside the official folder:
Classwork-08-Numerical-Integration/

* numerical_integration.py — The working Python program organized with professional structural comments (# INPUT, # PROCESS, and # OUTPUT).
* PPP.txt — The complete and structured pseudocode following strict class rules (Plain English, ← for assignments, # for comments, and zero Python syntax).
* Flowchart.png — The exported flowchart diagram covering the iterative loop logic for each method and the decision-making flow for the selected modes.

---

## Implementation Details & Architecture

### 1. Preparation and Data Capture (Inputs)
* Dynamic Input Capture: The program interactively prompts the user for the integration limits (a and b), the function string, and the preferred numerical integration method.
* Smart Token Validation: A built-in validation mechanism processes the constant pi. If the user inputs "pi", the code automatically invokes the .replace() function to substitute the text with the exact numerical value from the standard math library (math.pi).
* Step Size Calculation: Once the boundaries are established, the step size h (representing the width or base of each subinterval) is calculated using the standard formula:
  h = (b - a) / n

### 2. Optimization of the Rectangular Methods (LRM, RRM, MRM)
To enforce DRY (Don't Repeat Yourself) principles and optimize computational efficiency, the development unified the logic of the three rectangular methods into a single, cohesive structure instead of writing three independent loops. This was achieved using shift and constant variables:

* LRM (Left Riemann Sum): The loop starts without alterations (shift = 0), evaluating the height of the rectangle precisely at the left edge of each subinterval.
* RRM (Right Riemann Sum): The evaluation point shifts forward by one index (shift = 1), evaluating the height at the right edge of each subinterval.
* MRM (Midpoint Riemann Sum): A continuous displacement factor (constant = h / 2) is injected into the position variable. This shifts the evaluation point exactly to the geometric center of the subinterval prior to calculating its height.

### 3. Trapezoid Method Implementation (TRAP)
Because the trapezoidal approach relies on a fundamentally different geometric structure compared to flat rectangles, its algorithm is handled separately:
1. Endpoint Evaluation: The code first isolates, evaluates, and stores the values of the outer boundaries (f(a) and f(b)).
2. Intermediate Height Summation: A dedicated loop iterates through all intermediate segments, doubling their weights (2 * f(x_i)) to strictly comply with the mathematical trapezoidal rule.

---

## Environment and Tools

* Language: Python
* Version Control: Git
* Hosting & Collaboration Platform: GitHub

## AI Use Declaration
AI tools were used exclusively to assist in drafting, formatting, and refining this README.md file. No AI tools or code assistants were used for writing the actual source code (numerical_integration.py), creating the pseudocode (PPP.txt), designing the flowchart (Flowchart.png), or setting up the Git/GitHub environment. All programming logic and deliverables were developed entirely by me.
