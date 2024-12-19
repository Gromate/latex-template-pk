# LaTeX Thesis Template for Politechnika Krakowska

This repository provides a LaTeX template for students of Politechnika Krakowska to write their theses. It includes a structured main file, a customizable title page, and a Python script to apply formatting that does not work with basic LaTeX. The template is designed to be compatible with Overleaf for online editing.

## Features

- **Structured LaTeX Files**:
  - `main.tex`: The main file for writing the thesis.
  - `titlepage.tex`: Customize the title page according to university standards.
  - `sample.bib`: A sample bibliography file to manage references.
- **Formatting Script**:
  - `fix_single_letter_words.py`: A Python script to prevent single-letter words from being left at the end of a line.
- **Resource Folder**:
  - `media/`: Contains additional resources, such as images or diagrams, for your thesis.

## Installation and Usage

### Using the Template on Overleaf
1. Download the repository as a ZIP file.
2. Upload the contents to Overleaf.
3. Edit `main.tex` to start writing your thesis.
4. Customize `titlepage.tex` to reflect your thesis details.
5. Include your references in `sample.bib`.

### Running the Python Script
The `fix_single_letter_words.py` script ensures single-letter words are not left at the end of a line, enhancing document readability.

#### Requirements
- Python 3.x

#### Usage
1. Run the script with the command:
   ```bash
   python fix_single_letter_words.py
   ```
2. The script will process your `.tex` files and fix formatting issues.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues.

## Authors
- Mateusz Grochowski [@Gromate](https://github.com/Gromate)
- Bartosz Bizoń [@bartekbiz](https://github.com/bartekbiz)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to PhD, Eng Paweł Lempa [@PKPL](https://github.com/PKPL) for providing guidelines that helped shape this template.
