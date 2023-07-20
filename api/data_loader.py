import pandas as pd
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

def read_excel_files(*file_paths):
    data = pd.DataFrame()
    for file_path in file_paths:
        df = pd.read_excel(file_path)
        df['Preprocessed_Description'] = df['Description'].apply(preprocess_text)
        data = data.append(df, ignore_index=True)
    return data

def write_to_csv(file_path, data):
    data.to_csv(file_path, index=False)
