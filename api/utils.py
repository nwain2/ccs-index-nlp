import csv
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# NLTK text preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join tokens back to text
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

def compare_column_counts(file_path, column1, column2):
    """Compares the count of two columns in an excel or csv file"""
    count1 = 0
    count2 = 0
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            count1 += 1 if preprocess_text(row[column1]) else 0
            count2 += 1 if preprocess_text(row[column2]) else 0
        return count1 == count2

def compare_column_values(file_path, column1, column2):
    """Compares the values of two columns in an excel or csv file"""
    values1 = set()
    values2 = set()
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            values1.add(preprocess_text(row[column1]))
            values2.add(preprocess_text(row[column2]))
        return values1 == values2

def load_model(model_path):
    """Loads the given model from the given path"""
    model = None
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model
