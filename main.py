import pandas as pd
from api.nlp_api import some_function_in_nlp_api
from api.data_loader import read_excel_files, write_to_csv
from reporting.pdf_generator import generate_pdf
from api.analyze_data import calculate_relevancyy

def main():
    # Call NLP functions
    nlp_results = some_function_in_nlp_api()
    
    # Read data from Excel files
    data = read_excel_files("data/test_file1.xlsx", "data/test_file2.xlsx")
    
    # Perform NLP analysis on data and get results
    nlp_results = some_function_in_nlp_api(data)
    
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
