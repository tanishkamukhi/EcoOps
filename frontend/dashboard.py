import streamlit as st
import matplotlib.pyplot as plt
from backend.offset_calc import calculate_offsets
from backend.vendor_api import plant_tree_api
from backend.report_gen import generate_csv_report, generate_pdf_report

def show_dashboard(df):
    st.header("🚗 Travel Footprint Calculator")

    # User Inputs
    user_id = st.text_input("Enter User ID", value="U001")
    name = st.text_input("Enter Your Name", value="Demo User")

    distance = st.number_input("Enter travel distance (in km)", min_value=0.0, step=10.0)
    mode = st.selectbox("Select mode of transport", ["Car", "Bus", "Train", "Flight", "Bike"])

    if st.button("Calculate Footprint"):
        emissions, trees_needed = calculate_offsets(distance, mode)
        st.success(f"🌍 CO2 Emissions: {emissions:.2f} kg")
        st.info(f"🌳 Trees required: {trees_needed}")

        # Save history
        df.loc[len(df)] = {
            "User ID": user_id,
            "Name": name,
            "Distance (km)": distance,
            "Mode": mode,
            "Emissions (kg CO2)": emissions,
            "Trees": trees_needed
        }

    # Tree Planting Section
    st.subheader("🌳 Offset Your Carbon Footprint")
    trees = st.number_input("How many trees to plant?", min_value=1, step=1)
    vendor = st.selectbox("Choose Vendor", ["EcoOps Demo Vendor", "Grow-Trees", "SankalpTaru"])

    if st.button("Plant Trees"):
        response = plant_tree_api(user_id=user_id, trees=trees, vendor=vendor)
        st.write(f"Vendor Response: {response}")

    # History Table
    st.subheader("📊 Your Calculation History")
    st.dataframe(df)

    # Chart
    if not df.empty:
        st.subheader("📈 Emissions Chart")
        fig, ax = plt.subplots()
        ax.bar(df["Mode"], df["Emissions (kg CO2)"], color="green")
        ax.set_ylabel("Emissions (kg CO2)")
        ax.set_xlabel("Mode of Transport")
        ax.set_title("Carbon Emissions by Mode")
        st.pyplot(fig)

    # Report Section
    st.subheader("📝 Generate & Download Reports")

    # CSV Report
    if st.button("Generate CSV Report"):
        filepath = generate_csv_report(df)
        with open(filepath, "rb") as f:
            st.download_button("⬇️ Download CSV", f, file_name=filepath, mime="text/csv")
        st.success(f"✅ CSV Report generated: {filepath}")

    # PDF Report
    if st.button("Generate PDF Report"):
        filepath = generate_pdf_report(df)
        with open(filepath, "rb") as f:
            st.download_button("⬇️ Download PDF", f, file_name=filepath, mime="application/pdf")
        st.success(f"✅ PDF Report generated: {filepath}")
