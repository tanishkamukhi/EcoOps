import streamlit as st
from backend.carbon_calc import calculate_travel_footprint
from backend.suggestion_engine import get_suggestions
from backend.vendor_api import plant_tree_api
from frontend.charts import plot_footprint_chart

def show_dashboard():
    st.title("🌍 EcoOps - Automated Sustainability Agent")

    # --- Travel Input Form ---
    st.subheader("✈️ Travel Footprint Calculator")
    distance = st.number_input("Enter travel distance (in km):", min_value=0.0, step=1.0)
    mode = st.selectbox("Select mode of transport:", ["Car", "Bus", "Flight"])

    if "footprint" not in st.session_state:
        st.session_state.footprint = None
    if "plant_response" not in st.session_state:
        st.session_state.plant_response = None

    if st.button("Calculate Footprint"):
        st.session_state.footprint = calculate_travel_footprint(distance, mode)
        st.session_state.plant_response = None  # reset tree response

    if st.session_state.footprint is not None:
        footprint = st.session_state.footprint
        st.success(f"✅ Your travel footprint: {footprint:.2f} kg CO₂")

        # Chart
        plot_footprint_chart(footprint)

        # Suggestions
        st.subheader("🌱 Eco-Friendly Suggestions")
        tips = get_suggestions(footprint)
        for tip in tips:
            st.write(f"- {tip}")

        # Vendor API (tree planting)
        st.subheader("🌳 Offset Your Carbon Footprint")
        trees = st.number_input("How many trees to plant?", min_value=1, step=1)
        user_id = "demo_user"  # static user for now

        if st.button("Plant Trees"):
            st.session_state.plant_response = plant_tree_api(user_id, int(trees))

        if st.session_state.plant_response:
            st.json(st.session_state.plant_response)
