import streamlit as st
import pandas as pd

def analytics_dashboard():
    st.title("📈 Analytics Dashboard")

    # Choose visualization type
    option = st.radio("Select Visualization:", ["Streamlit Chart", "Power BI Report"])

    if option == "Streamlit Chart":
        # Example dummy data
        data = {
            "Product": ["Milk", "Bread", "Biscuits", "Juice"],
            "Complaints": [12, 5, 8, 3]
        }
        df = pd.DataFrame(data)

        st.subheader("Complaints by Product")
        st.bar_chart(df.set_index("Product"))

    elif option == "Power BI Report":
        st.subheader("Embedded Power BI Report")
        # Replace this URL with your Power BI Publish-to-Web link
        power_bi_url = "https://app.powerbi.com/view?r=YOUR_REPORT_ID"
        st.markdown(f'<iframe width="100%" height="600" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
