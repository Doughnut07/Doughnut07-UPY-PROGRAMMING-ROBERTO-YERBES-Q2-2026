# Unit 3: Programming Assignment – The Mandelbrot Set

This repository contains a Python-based implementation developed as part of Unit 3 for the Programming course (Q2-2026).

The primary objective of this assignment is to implement the computational logic behind the **Mandelbrot Set** by reading configurable parameters from an external file, mapping a grid of pixels into the complex plane, computing the number of iterations required for each point to escape, and exporting the results into a CSV file for future visualization.

---

## Project Description

### The Mandelbrot Set

The objective of this application is to calculate how many iterations each point of a two-dimensional grid requires before escaping the Mandelbrot condition. Every point on the grid is converted into a complex number, and the recursive formula is repeatedly applied until either the point escapes or the maximum number of iterations is reached.

Instead of generating an image directly, this program stores the computed data inside a CSV file. This approach simulates a real-world data pipeline, where numerical computations are performed first and visualizations are generated later from the exported dataset.

---

## Repository Structure

All deliverables for this assignment are located inside the official folder:

`Classwork-11-The-Mandelbrot-Set/`

* `mandelbrot.py` — The Python implementation organized using professional structural comments (`# INPUT`, `# PROCESS`, and `# OUTPUT`).
* `PPP.txt` — The complete pseudocode written in Plain English following the class conventions (`←` assignments, `#` comments, and no Python syntax).
* `Flowchart.png` — The complete flowchart illustrating the configuration loading process, nested iteration loops, Mandelbrot calculations, and CSV export workflow.

---

## Implementation Details & Architecture

### 1. Configuration Loading

The program begins by opening the `config.txt` file and reading each configuration parameter line by line.

Each line is separated using the `=` character and stored inside a dictionary, allowing every numerical parameter to be accessed by its corresponding key without hardcoding any values into the program.

### 2. Grid Mapping (PROCESS)

Once the configuration has been loaded, the program extracts the grid dimensions (`ancho` and `alto`) along with the maximum iteration limit.

Two nested `for` loops traverse every row and column of the grid. Each coordinate is mathematically transformed into its corresponding complex number (`c`) using the configured real and imaginary ranges.

### 3. Mandelbrot Iteration

For every complex point:

* The variable `z` starts at the complex value `0 + 0j`.
* An iteration counter starts at zero.
* A `while` loop repeatedly evaluates the Mandelbrot equation:

  `z = z² + c`

The loop continues while:

* The magnitude of `z` remains less than or equal to 2.
* The iteration counter has not exceeded the configured maximum number of iterations.

The final iteration count represents how quickly that point escapes from the Mandelbrot set.

### 4. CSV Output (OUTPUT)

After computing the iteration count for each grid position, the program writes one record into the output CSV file using the following format:

`fila,columna,iteraciones`

Once every point has been processed, the output file is closed and the program displays the confirmation message:

`Done`

---

## Environment and Tools

* **Language:** Python
* **Version Control:** Git
* **Hosting & Collaboration Platform:** GitHub

---

## AI Use Declaration

AI tools were used to assist in designing the **Flowchart.png**, translating the program logic into a structured visual representation. AI was also consulted during the development of the project to support the creation of the pseudocode, improve code organization, and assist in documenting the project through this README while preserving the original algorithm and assignment requirements.
