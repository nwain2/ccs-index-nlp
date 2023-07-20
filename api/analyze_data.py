import pandas as pd
import nltk
nltk.download('punkt')

def preprocess_text(text):
    if pd.isnull(text):  # Handle NaN values
        return ""

    if not isinstance(text, str):  # Handle non-string values
        return ""

    tokens = nltk.word_tokenize(text)
    # Add the rest of your preprocessing steps here, if any
    return " ".join(tokens)

def calculate_relevancy(group):
    # Calculate the mean sentiment and relevancy scores for each group
    # You can replace this with the relevant code or API for sentiment analysis and relevancy scoring
    # For now, we'll just set them to dummy values
    group['Sentiment'] = 0.5
    group['Relevancy'] = 0.7
    return group

# Load the data from the Excel file
data = pd.read_csv("data/cyber_security_data.csv", encoding='ISO-8859-1', error_bad_lines=False)


# Preprocess the 'Description' column using NLTK
data['Preprocessed_Description'] = data['Description'].apply(preprocess_text)

# Set up the NLP API client (replace this with your chosen NLP API or library for sentiment analysis and relevancy scoring)
class NLPAPI:
    def __init__(self):
        pass  # Replace this with the initialization of your chosen NLP API or library

    def get_sentiment(self, text):
        return 0.5  # Replace this with the appropriate sentiment analysis result from your chosen NLP API

    def get_relevancy(self, text):
        return 0.7  # Replace this with the appropriate relevancy score from your chosen NLP API

nlp_api = NLPAPI()

# Group data based on Taxonomy and Attack Class and calculate relevancy
grouped_data = data.groupby(['Taxonomy', 'Attack Class']).apply(calculate_relevancy)

# Calculate the mean relevancy for each Taxonomy and Attack Class
grouped_data = grouped_data.groupby(['Taxonomy', 'Attack Class']).agg({
    'Relevancy': 'mean',
    'Sentiment': 'mean'  # You can calculate the mean sentiment as well if needed
}).reset_index()

grouped_data = data.groupby('Country')
count_per_country = grouped_data['Relevancy'].count()

# Calculations based on grouped_data DataFrame:

# Count of Occurrences:
# Number of attacks per country, taxonomy, and attack class
count_per_country = grouped_data.groupby('Country')['Relevancy'].count()
count_per_taxonomy = grouped_data.groupby('Taxonomy')['Relevancy'].count()
count_per_attack_class = grouped_data.groupby('Attack Class')['Relevancy'].count()

# Frequency and Percentage:
# Percentage of attacks from each country compared to the total number of attacks
total_attacks = grouped_data['Relevancy'].count()

# Percentage of attacks belonging to each taxonomy and attack class
percentage_per_taxonomy = count_per_taxonomy / total_attacks * 100
percentage_per_attack_class = count_per_attack_class / total_attacks * 100

# Average and Mean:
# Average number of attacks per country, taxonomy, and attack class
average_attacks_per_country = count_per_country.mean()
average_attacks_per_taxonomy = count_per_taxonomy.mean()
average_attacks_per_attack_class = count_per_attack_class.mean()

# Summation:
# Total number of attacks from each country, taxonomy, and attack class
total_attacks_per_country = grouped_data.groupby('Country')['Relevancy'].sum()
total_attacks_per_taxonomy = grouped_data.groupby('Taxonomy')['Relevancy'].sum()
total_attacks_per_attack_class = grouped_data.groupby('Attack Class')['Relevancy'].sum()

# Ranking:
# Rank countries based on the number of attacks they experienced
country_ranking = total_attacks_per_country.rank(ascending=False)

# Rank taxonomies based on the average relevancy scores of attacks in each category
taxonomy_ranking = average_attacks_per_taxonomy.rank(ascending=False)

# Distribution Analysis:
# Use data visualization libraries to plot histograms or box plots to visualize the distribution of sentiment or relevancy scores for different taxonomies or attack classes.

# Correlation:
# Calculate the correlation between the number of attacks and the sentiment or relevancy scores

# Time Series Analysis:
# If applicable, analyze trends over time for specific fields. For example, analyze the trend of attacks per month or year.

# Percentage Change:
# Calculate the percentage change in the number of attacks in a specific country compared to the previous year

# Save the results to a new CSV file
grouped_data.to_csv("grouped_data_with_relevancy.csv", index=False)
