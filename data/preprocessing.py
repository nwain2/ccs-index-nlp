import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sys

def preprocess_text(text):
    #remove special characters and numbers
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    #convert to lowercase
    text = text.lower()
    #tokenization
    tokens = nltk.word_tokenize(text)
    #remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    #lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    #join tokens back to text
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

if __name__ == "__main__":
    #get input from the command line
    input_text = input("Enter the text to preprocess: ")
    preprocessed_text = preprocess_text(input_text)
    print("Preprocessed Text:", preprocessed_text)
