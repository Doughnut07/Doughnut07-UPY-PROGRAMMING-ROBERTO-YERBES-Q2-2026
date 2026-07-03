# Unit 3: Programming Assignment – The Mandelbrot Set Visualization

This repository contains a Python-based implementation developed as part of Unit 3 for the Programming course (Q2-2026).

The primary objective of this assignment is to transform the numerical data generated in the previous Mandelbrot assignment into a visual representation by reading the CSV file, converting iteration counts into pixel brightness values, and generating a PNG image using the Pillow (PIL) library.

---

## Project Description

### The Mandelbrot Set Visualization

The objective of this application is to convert the raw numerical results obtained from the Mandelbrot computation into a graphical image.

The program loads the iteration data previously stored in a CSV file, normalizes every iteration count into a brightness value between **0** and **255**, assigns the corresponding color to each pixel, and finally saves the generated image as a PNG file.

This assignment demonstrates an important concept in Data Science: separating numerical computation from data visualization by storing intermediate results before rendering them into an image.

---

## Repository Structure

All deliverables for this assignment are located inside the official folder:

`Classwork-12-The-Mandelbrot-Visualization/`

* `mandelbrot_visualization.py` — The Python implementation organized using professional structural comments (`# INPUT`, `# PROCESS`, and `# OUTPUT`).
* `PPP.txt` — The complete pseudocode written in Plain English following the class conventions (`←` assignments, `#` comments, and no Python syntax).
* `Flowchart.png` — The complete flowchart illustrating the configuration loading, CSV parsing, brightness calculation, pixel generation, and image export workflow.
* `config.txt` — Configuration file containing the image dimensions and Mandelbrot parameters.
* `clase.csv` — Input dataset generated during Classwork #11 containing every pixel position and its corresponding iteration count.
* `mandelbrot-clase.png` — Final image generated from the CSV data.

---

## Implementation Details & Architecture

### 1. Configuration Loading

The program begins by opening the `config.txt` file and reading every configuration parameter into a dictionary.

Each value is automatically converted into either an integer or a decimal depending on its format, allowing the program to retrieve the image dimensions and maximum iteration value without hardcoding any constants.

### 2. CSV Processing (PROCESS)

The application opens the `clase.csv` file and reads all its contents into memory.

The first row, which contains the column headers, is discarded, while each remaining record is processed individually by separating:

* Row (`fila`)
* Column (`columna`)
* Iteration count (`iteraciones`)

These values are converted into integers before continuing with the visualization process.

### 3. Brightness Calculation

For every pixel, the program determines its brightness according to the number of iterations required for the corresponding complex point to escape.

* If the point reached the maximum number of iterations, the brightness is set to **0**, representing points inside the Mandelbrot set.
* Otherwise, the iteration count is normalized into a value between **0** and **255**, producing different brightness levels based on how quickly the point escaped.

### 4. Image Generation (OUTPUT)

A new image is created using the **HSV** color model provided by the Pillow library.

Each processed pixel is written into its corresponding position using the calculated brightness value.

After all pixels have been assigned, the image is converted to the **RGB** color model and saved as:

`mandelbrot-clase.png`

Finally, the program displays the confirmation message:

`DONE`

---

## Environment and Tools

* **Language:** Python
* **External Library:** Pillow (PIL)
* **Version Control:** Git
* **Hosting & Collaboration Platform:** GitHub

---

## AI Use Declaration

AI tools were used to assist in designing the **Flowchart.png**, helping convert the program's logic into a structured visual representation. AI was also consulted during the preparation of the project documentation, the development of the pseudocode, and for organizational support while implementing the CSV parsing and image generation workflow using the Pillow library.
