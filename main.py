from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import fitz  # PyMuPDF
import re
from collections import defaultdict
from docx import Document

app = Flask(__name__)
CORS(app)

try:
    nlp = spacy.load('C:\\Users\\mitam\\Documents\\Visual Studio\\internship\\final\\output\\model-best')
except Exception as e:
    app.logger.error(f"Failed to load spaCy model: {e}")
    raise e

phone_pattern = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

def process_text(text, nlp):
    data = defaultdict(set)  # Use set to avoid duplicates
    spacy_doc = nlp(text)
    for ent in spacy_doc.ents:
        data[ent.label_].add(ent.text)
    phones = phone_pattern.findall(text)
    emails = email_pattern.findall(text)
    for phone in phones:
        data["PHONE"].add(phone)
    for email in emails:
        data["EMAIL"].add(email)
    return {key: list(values) for key, values in data.items()}  # Convert to list for JSON serialization

def parse_docx(file):
    doc = Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def parse_pdf(file):
    doc = fitz.open(stream=file.read(), filetype='pdf')
    text = ''
    for page in doc:
        text += page.get_text("text")
    return text

@app.route('/parse', methods=['POST'])
def parse_files():
    try:
        files = request.files.getlist('files')
        all_data = []
        for file in files:
            filename = file.filename
            try:
                if filename.lower().endswith('.pdf'):
                    text = parse_pdf(file)
                elif filename.lower().endswith('.docx'):
                    text = parse_docx(file)
                else:
                    return jsonify({'error': f'Unsupported file format: {filename}'}), 400

                file_data = process_text(text, nlp)
                all_data.append({'filename': filename, **dict(file_data)})  # Include filename in the data
            except Exception as e:
                app.logger.error(f"Failed to process file {filename}: {e}")
                return jsonify({'error': f'Failed to process file {filename}: {e}'}), 500
        return jsonify(all_data)
    except Exception as e:
        app.logger.error(f"Error in parse_files: {e}")
        return jsonify({'error': f'Error in parse_files: {e}'}), 500

if __name__ == '__main__':
    app.run(port=5000)
