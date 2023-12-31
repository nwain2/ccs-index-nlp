import os
import pandas as pd
import reportlab.pdfgen.canvas as canvas
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    preprocessed_text = ' '.join(lemmatized_tokens)
    return preprocessed_text

def generate_pdf(data, filename):
    """Generates a PDF file from the given data"""
    pdf = canvas.Canvas(filename)
    pdf.setTitle("Cyber Security Report")
    data['Preprocessed_Description'] = data['Description'].apply(preprocess_text)
    data.to_pdf(pdf)
    pdf.save()
