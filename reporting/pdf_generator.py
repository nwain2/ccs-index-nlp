import os
import pandas as pd
import reportlab.pdgen.canvas as canvas

def generate_pdf(data, filename):
    """Generates a PDF file from the given data"""
    pdf = canvas.Canvas(filename)
    pdf.setTitle("Cyber Security Report")
    data.to_pdf(pdf)
    pdf.save()

if __name__ == "__main__":
    data = pd.read_csv("data/cyber_security_data.csv")
    generate_pdf(data, "cyber_security_report.pdf")
