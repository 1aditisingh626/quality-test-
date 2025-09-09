import streamlit as st

def complaint_tracker():
    st.title("🔎 Complaint Tracker")

    complaint_id = st.text_input("Enter Complaint ID")
    if st.button("Track Status"):
        if complaint_id:
            st.info(f"Complaint #{complaint_id} is currently under review 🚀")
        else:
            st.warning("Please enter a Complaint ID.")
