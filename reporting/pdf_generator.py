import os
import pandas as pd
from reportlab.pdfgen import canvas

def generate_pdf(data, filename):
    """Generates a PDF file from the given data"""
    pdf = canvas.Canvas(filename)
    pdf.setTitle("Cyber Security Report")

    # Convert data to a string representation (assuming you want to write the data to the PDF)
    data_str = data.to_string()

    # Write the data to the PDF
    pdf.drawString(100, 700, "Cyber Security Report")
    pdf.drawString(100, 680, data_str)  # You may need to adjust the coordinates as per your layout

    pdf.save()

if __name__ == "__main__":
    data = pd.read_csv("data/cyber_security_data.csv")
    generate_pdf(data, "cyber_security_report.pdf")

