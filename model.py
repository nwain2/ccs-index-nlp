import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

#load the preprocessed data from a CSV file
data = pd.read_csv('data/cyber_security_data.csv')

#split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(data['text'], data['category'], test_size=0.2, random_state=42)

#preprocess the training and testing data
train_data_preprocessed = train_data.apply(preprocess_text)
test_data_preprocessed = test_data.apply(preprocess_text)

#create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(train_data_preprocessed)
test_vectors = vectorizer.transform(test_data_preprocessed)

#train an SVM classifier
svm = SVC()
svm.fit(train_vectors, train_labels)

#predict the labels for the test data
predictions = svm.predict(test_vectors)

#print classification report
print(classification_report(test_labels, predictions))
