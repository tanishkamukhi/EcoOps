import streamlit as st
from frontend.dashboard import show_dashboard

def main():
    st.sidebar.title("🌿 EcoOps Navigation")
    page = st.sidebar.radio("Go to:", ["Dashboard"])

    if page == "Dashboard":
        show_dashboard()

if __name__ == "__main__":
    main()
