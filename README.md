README.md is a Markdown file that shows up as a description in your GitHub repo. Here we include instructions for anyone to run the code. Edit this file with your own names and text.

# [Project Title]

![Example final poster](example_poster.svg)

**Created by:** [Student 1], [Student 2], [Student 3], [Student 4]  
**Course:** Creative Coding, Pratt Institute  
**Semester:** Fall 2026

## About the Project

[Write a short description of your project. What was the idea behind your poster generator? What visual qualities or design ideas inspired it? How does the program combine everyone's individual tile designs into a unified composition?]

## The Design

Our poster generator creates a grid of geometric tiles using a collection of custom-designed functions. Each tile can be rotated, colored, and positioned according to its location in the grid. Users can choose the dimensions of the poster and select from a collection of color palettes, or generate a random palette.

## Meet the Designers

- **[Student 1]:** [Brief description of their tile designs or contribution.]
- **[Student 2]:** [Brief description of their tile designs or contribution.]
- **[Student 3]:** [Brief description of their tile designs or contribution.]
- **[Student 4]:** [Brief description of their tile designs or contribution.]

## Try it yourself

Copy this code into a Colab Notebook!

```python
!git clone https://github.com/sarahchase/cc-f26-group-project.git
%cd cc-f26-group-project
!pip install -r requirements.txt

from project import generate_poster
generate_poster()
```

Or click below to open an example notebook in Google Colab and generate your own poster!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iho7fD12AxIXqKzoNI5bAI-NxnKauBgz?usp=sharing)

### How to Use

1. Open the notebook in Google Colab.
2. Run the setup cells to download the project code and install the required libraries.
3. Run the cell that calls the function and prompts the user to choose a title, grid dimensions, and color palette.
4. Your own poster will be saved as poster.svg!

## Files

- `project.py` – Main poster-generation program.
- `TileFunctions.py` – Collection of custom tile-drawing functions.
- `PaletteOptions.py` – Available color palettes.
- `requirements.txt` – Required Python libraries.
- `example_poster.svg` – Scalable vector version of an example final poster image.

