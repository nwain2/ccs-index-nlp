import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# NLTK text preprocessing function
def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join tokens back to text
    preprocessed_text = ' '.join(lemmatized_tokens)
    return preprocessed_text

# Replace NLPAPI import with NLTK-based text preprocessing
class NLPAPI:
    def preprocess_text(self, text):
        return preprocess_text(text)

# Now you can use NLPAPI for text preprocessing with NLTK
nlp_api = NLPAPI()

# Example usage
text = "This is a sample text for preprocessing with NLTK."
preprocessed_text = nlp_api.preprocess_text(text)
print("Preprocessed Text:", preprocessed_text)
