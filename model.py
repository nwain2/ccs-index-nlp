import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from api.preprocessing import preprocess_text

def train_and_evaluate_model():
    # Load the preprocessed data from a CSV file
    data = pd.read_csv('data/cyber_security_data.csv')

    # Split the data into training and testing sets
    train_data, test_data, train_labels, test_labels = train_test_split(data['text'], data['category'], test_size=0.2, random_state=42)

    # Preprocess the training and testing data
    train_data_preprocessed = train_data.apply(preprocess_text)
    test_data_preprocessed = test_data.apply(preprocess_text)

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    train_vectors = vectorizer.fit_transform(train_data_preprocessed)
    test_vectors = vectorizer.transform(test_data_preprocessed)

    # Train an SVM classifier
    svm = SVC()
    svm.fit(train_vectors, train_labels)

    # Predict the labels for the test data
    predictions = svm.predict(test_vectors)

    # Print classification report
    print(classification_report(test_labels, predictions))

if __name__ == "__main__":
    train_and_evaluate_model()
