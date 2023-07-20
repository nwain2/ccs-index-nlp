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


def read_csv_files(*file_paths):
    """
    Reads data from CSV files and returns a concatenated DataFrame.
    Args:
        *file_paths (str): Variable length list of file paths.
    Returns:
        pandas.DataFrame: Concatenated DataFrame from the CSV files.
    """
    data_frames = []
    for file_path in file_paths:
        data_frame = pd.read_csv(file_path)
        data_frames.append(data_frame)
    return pd.concat(data_frames)

def write_to_csv(file_path, data):
    """
    Writes data to a CSV file.
    Args:
        file_path (str): The path of the CSV file to write.
        data (pandas.DataFrame): The data to be written to the CSV file.
    """
    data.to_csv(file_path, index=False)
