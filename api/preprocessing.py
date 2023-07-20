import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

nltk.download('punkt')

# NLTK text preprocessing function
def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenization
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join tokens back to text
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

# Example usage
text = "This is a sample text for preprocessing with NLTK."
preprocessed_text = preprocess_text(text)
print("Preprocessed Text:", preprocessed_text)
