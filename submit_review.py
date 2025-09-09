import streamlit as st

def submit_review():
    st.title("✍️ Submit Review / Complaint")

    product = st.text_input("Enter Product Name")
    review = st.text_area("Your Review / Complaint")
    uploaded_file = st.file_uploader("Upload supporting file (image/doc)", type=["jpg", "png", "pdf", "docx"])

    if st.button("Submit"):
        if product and review:
            st.success(f"✅ Complaint/Review for **{product}** submitted successfully!")
        else:
            st.error("⚠️ Please fill in all required fields.")
