# Resume NLP Pipeline
### Automated Resume Screening System | Python · spaCy · NLTK · NER

Built during my product analytics internship at ZipBooks Software Solutions (2024).

## The Problem
Resume screening was manual, inconsistent, and slow — taking recruiters 3.5+ hours per day to shortlist candidates from 500+ diverse resume formats.

## What I Built
An end-to-end NLP pipeline that:
- Extracts structured data from unformatted resumes using spaCy and NLTK
- Uses Named Entity Recognition (NER) to identify skills, experience, and education
- Handles scanned PDFs via Tesseract OCR integration
- Scores and ranks candidates automatically based on job requirements

## Results
- 85%+ field extraction accuracy across 500+ resume formats
- 70% reduction in recruiter time-to-shortlist (~3.5 hrs/day saved)
- 3× applicant throughput per sprint without adding headcount
- Eliminated entire category of unprocessable scanned resumes

## Tech Stack
Python · spaCy · NLTK · Tesseract OCR · PDFMiner · Regex · Jupyter Notebook

## Project Structure
- `Resume Parser/` — main pipeline code
- `nlp_model/` — trained NER model with vocab and tokenizer
- `main.py` — entry point
- `final.ipynb` — development notebook with analysis

## About
Mit Mehta | MSMRA @ MSU Eli Broad | github.com/MightyMIT10
