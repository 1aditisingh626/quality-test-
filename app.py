import streamlit as st

# Import your page functions
from pages.homepage import homepage
from pages.submit_review import submit_review
from pages.complaint_tracker import complaint_tracker
from pages.vendor_dashboard import vendor_dashboard
from pages.analytics_dashboard import analytics_dashboard


# Dictionary of pages
PAGES = {
    "Homepage": homepage,
    "Submit Review/Complaint": submit_review,
    "Complaint Tracker": complaint_tracker,
    "Vendor Dashboard": vendor_dashboard,
    "Analytics Dashboard": analytics_dashboard
}

# Streamlit config
st.set_page_config(page_title="Product Quality Review Platform", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run the selected page
page = PAGES[selection]
page()
