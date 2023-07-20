import pandas as pd
from api.preprocessing import preprocess_text
from api.nlp_api import NLPAPI

def calculate_relevancy(group):
    # Calculate the mean sentiment and relevancy scores for each group
    group['Sentiment'] = group['Preprocessed_Description'].apply(nlp_api.get_sentiment)
    group['Relevancy'] = group['Preprocessed_Description'].apply(nlp_api.get_relevancy)
    return group

# Load the data from the Excel file
data = pd.read_excel("data/cyber_security_data.xlsx")

# Preprocess the 'Description' column
data['Preprocessed_Description'] = data['Description'].apply(preprocess_text)

# Set up the NLP API client
nlp_api = NLPAPI()

# Group data based on Taxonomy and Attack Class and calculate relevancy
grouped_data = data.groupby(['Taxonomy', 'Attack Class']).apply(calculate_relevancy)

# Calculate the mean relevancy for each Taxonomy and Attack Class
grouped_data = grouped_data.groupby(['Taxonomy', 'Attack Class']).agg({
    'Relevancy': 'mean',
    'Sentiment': 'mean'  # You can calculate the mean sentiment as well if needed
}).reset_index()

# Perform high-level arithmetic or any other calculations based on the grouped_data DataFrame to find differences in relevancy scores, etc.
# For example, you can calculate the difference in relevancy scores between different groups.

# Save the results to a new CSV file
grouped_data.to_csv("grouped_data_with_relevancy.csv", index=False)
