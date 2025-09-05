import streamlit as st
import matplotlib.pyplot as plt
from backend.carbon_calc import calculate_footprint
from backend.suggestions import suggest_actions
from backend.reporting import generate_report
from backend.vendors import connect_vendor

def show_dashboard():
    st.set_page_config(page_title="EcoOps – Sustainability Agent", layout="wide")
    st.title("🌱 EcoOps – Automated Sustainability Agent")
    st.markdown("Track your carbon footprint, get tips & generate report.")

    st.sidebar.header("Your Usage Details")
    electricity = st.sidebar.number_input("Electricity (kWh)", 0.0)
    water = st.sidebar.number_input("Water (Liters)", 0.0)
    transport = st.sidebar.number_input("Transport (km)", 0.0)

    if st.sidebar.button("Calculate"):
        total, breakdown = calculate_footprint(electricity, water, transport)
        st.subheader(f"Total CO₂ Emissions: **{total:.2f} kg**")

        st.subheader("Breakup of Emissions")
        fig, ax = plt.subplots()
        ax.bar(breakdown.keys(), breakdown.values(), color=["#2ecc71", "#3498db", "#e74c3c"])
        ax.set_ylabel("kg CO₂")
        st.pyplot(fig)

        st.subheader("Suggestions")
        tips = suggest_actions(breakdown)
        for t in tips:
            st.write("-", t)

        if st.button("Generate Report"):
            generate_report(total, breakdown, tips)
            st.success("Report generated: `reports/sustainability_report.pdf`")

        if st.button("Offset Carbon"):
            resp = connect_vendor("tree_plantation", int(total // 10))
            st.info(resp["message"])
