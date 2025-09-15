import streamlit as st
from frontend.dashboard import show_dashboard
import pandas as pd

# Global history store
if "history" not in st.session_state:
    st.session_state["history"] = pd.DataFrame(columns=["User ID", "Name", "Distance (km)", "Mode", "Emissions (kg CO2)", "Trees"])

def main():
    st.set_page_config(page_title="🌿 EcoOps - Advanced Sustainability Agent", layout="wide")
    st.title("🌿 EcoOps - Advanced Sustainability Agent")

    # Call Dashboard
    show_dashboard(st.session_state["history"])

if __name__ == "__main__":
    main()
