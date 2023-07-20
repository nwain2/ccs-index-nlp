import pandas as pd
from api.nlp_api import NLPAPI
from api.data_loader import read_csv_files, write_to_csv
from api.analyze_data import calculate_relevancy
from reporting.pdf_generator import generate_pdf

def main():
    # Call NLP functions
    nlp_api = NLPAPI()
    text = "This is a sample text for sentiment analysis."
    sentiment_score = nlp_api.get_sentiment(text)
    print("Sentiment Score:", sentiment_score)

    # Read data from CSV files
    data = read_csv_files("data/cyber_security_data.csv")

    # Perform NLP analysis on data and get results
    nlp_results = nlp_api.some_function_in_nlp_api(data)

    # Write results to CSV
    write_to_csv("data/cyber_security_data.csv", nlp_results)

    # Perform data analysis and calculate relevancy
    data = pd.read_csv("data/cyber_security_data.csv")
    grouped_data = data.groupby(['Taxonomy', 'Attack Class']).apply(calculate_relevancy)
    grouped_data.to_csv("grouped_data_with_relevancy.csv", index=False)

    # Generate the report using the analyzed data
    generate_pdf("reporting/templates/report_template.html", grouped_data)

if __name__ == "__main__":
    main()
