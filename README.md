# GC Content DNA Analysis

## Description
This project is a basic bioinformatics exercise developed to analyze the GC content of DNA sequences using Python.

GC content refers to the percentage of guanine (G) and cytosine (C) nucleotides in a DNA sequence. This parameter is useful in molecular biology and bioinformatics because it can provide information about sequence composition and biological properties.

## Objectives
- Create a simple bioinformatics project structure in GitHub
- Apply version control using Git and GitHub
- Implement a Python script to calculate GC content
- Read input data from external files
- Document the project clearly using Markdown

## Project Structure
- `data/` : input data files
- `scripts/` : Python scripts
- `results/` : output results
- `docs/` : additional documentation

## Script
The main script of this project is:

`scripts/gc_content.py`

This script reads a DNA sequence from a file and calculates its GC content.

## Example
Example DNA sequence stored in:

`data/example_sequence.txt`

`ATGCGCGTAACCGGTT`

The script reads the sequence from the file and computes the percentage of G and C nucleotides.

### Expected Output

```
DNA sequence: ATGCGCGTAACCGGTT
GC Content: 62.50%
```

## How to Use
1. Clone or download the project    
2. Make sure the file `data/example_sequence.txt` contains a DNA sequence  
3. Run the script:

```
python3 scripts/gc_content.py
```

4. Read the GC content result in the terminal

## Technologies Used
- Python
- Git
- GitHub
- Markdown

## Author
Created as an academic project for the course *Introducción a la Programación Científica*.
