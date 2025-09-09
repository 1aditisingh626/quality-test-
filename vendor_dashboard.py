import streamlit as st

def vendor_dashboard():
    st.title("🏭 Vendor Dashboard")
    st.write("📊 Here vendors can see complaints, resolution status, and trust score.")

    # Example static data
    st.metric("Trust Score", "85%", delta="+5%")
    st.metric("Active Complaints", "12")
    st.metric("Resolved Complaints", "48")
