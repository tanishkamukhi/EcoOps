from fpdf import FPDF
import os
import pandas as pd

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "EcoOps Sustainability Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(df, filename="ecoops_report.pdf"):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Detailed Report", ln=True, align="L")
    pdf.ln(5)

    # ✅ Handle dataframe rows safely
    for _, row in df.iterrows():
        user = row.get("name", "Unknown")
        dist = row.get("distance", 0)
        mode = row.get("transport", "N/A")
        tree = row.get("tree", "Not Provided")

        pdf.multi_cell(
            0, 10,
            f"User: {user}\n"
            f"Distance Travelled: {dist} km\n"
            f"Mode of Transport: {mode}\n"
            f"Tree Selected: {tree}\n"
            
            "-----------------------------------"
        )
        pdf.ln(2)

    # ✅ Save file in project folder
    filepath = os.path.join(os.getcwd(), filename)
    pdf.output(filepath)

    return filepath
import pandas as pd
import os
from fpdf import FPDF

# --- PDF Class & generate_pdf_report पहले जैसा रहेगा ---

def generate_csv_report(df, filename="ecoops_report.csv"):
    """Generate a CSV report from dataframe"""
    filepath = os.path.join(os.getcwd(), filename)
    df.to_csv(filepath, index=False)
    return filepath
