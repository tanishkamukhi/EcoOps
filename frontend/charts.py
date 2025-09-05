import streamlit as st
import matplotlib.pyplot as plt

def plot_footprint_chart(footprint):
    """Displays a simple pie chart of CO2 footprint vs target"""
    target = 500  # example benchmark
    labels = ["Your Footprint", "Sustainable Target"]
    values = [footprint, max(0, target - footprint)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")

    st.pyplot(fig)
