import os
import pandas as pd
from fpdf import FPDF
from datetime import datetime

REPORT_DIR = "reports"

# Ensure reports folder exists
os.makedirs(REPORT_DIR, exist_ok=True)

def cleanup_old_reports():
    """Delete all old reports before generating new one."""
    for file in os.listdir(REPORT_DIR):
        file_path = os.path.join(REPORT_DIR, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print("⚠️ Error deleting file:", e)

def generate_csv_report(df: pd.DataFrame):
    """Generate and save CSV report, keeping only latest."""
    cleanup_old_reports()  # delete old reports
    filename = f"ecoops_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = os.path.join(REPORT_DIR, filename)
    df.to_csv(filepath, index=False)
    return filepath

def generate_pdf_report(df: pd.DataFrame):
    """Generate and save PDF report, keeping only latest."""
    cleanup_old_reports()  # delete old reports
    filename = f"ecoops_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(REPORT_DIR, filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="🌍 EcoOps Sustainability Report", ln=True, align="C")
    pdf.ln(10)

    # Table Header
    for col in df.columns:
        pdf.cell(40, 10, col, 1, 0, "C")
    pdf.ln()

    # Table Rows
    for _, row in df.iterrows():
        for item in row:
            pdf.cell(40, 10, str(item), 1, 0, "C")
        pdf.ln()

    pdf.output(filepath)
    return filepath
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  # Unicode font
        self.set_font("DejaVu", "", 12)

def generate_pdf_report(df):
    pdf = PDF()
    pdf.cell(0, 10, "EcoOps Report 🌍 - Tree Plantation", ln=True, align="C")

    for i, row in df.iterrows():
        pdf.cell(0, 10, f"Tree: {row['tree']}, Quantity: {row['quantity']}", ln=True)

    filepath = "ecoops_report.pdf"
    pdf.output(filepath)
    return filepath
