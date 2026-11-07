import streamlit as st
import pandas as pd
import csv
import os

st.set_page_config(
    page_title="Global Travel Survey",
    page_icon="🌍",
    layout="wide"
)
# PAGE TITLE
st.title("Global Travel Survey")
st.markdown("""
### Where would you like to travel?

Help us explore travel preferences around the world!

Select your dream destination and tell us how long
you would like to stay.
""")
st.divider()
# SURVEY FORM
st.subheader("Plan Your Dream Trip")

with st.form("travel_survey"):
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox(
            "Choose your dream destination",
            [
                "United States",
                "China",
                "India",
                "Japan",
                "Germany",
                "United Kingdom",
                "France",
                "Brazil",
                "Canada",
                "Australia"
            ]
        )
    with col2:
        days = st.slider(
            "How many days would you stay?",
            min_value=1,
            max_value=30,
            value=7
        )
    submitted = st.form_submit_button(
        "Submit My Trip",
        use_container_width=True
    )
    if submitted:
        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if os.path.getsize("data.csv") == 0:
                writer.writerow(["Category", "Value"])
            writer.writerow([country, days])
        st.success("Your dream trip has been added!")
        st.balloons()

# CURRENT DATA
st.divider()
st.subheader("Explore Survey Responses")
if os.path.exists("data.csv"):
    data = pd.read_csv("data.csv")
    if not data.empty:
        data["Value"] = pd.to_numeric(
            data["Value"],
            errors="coerce"
        )
        data = data.dropna(subset=["Value"])
        col3, col4, col5 = st.columns(3)
        with col3:
            st.metric(
                "Total Responses",
                len(data)
            )
        with col4:
            st.metric(
                "Average Trip Length",
                f"{data['Value'].mean():.1f} days"
            )
        with col5:
            st.metric(
                "Unique Destinations",
                data["Category"].nunique()
            )
        st.write("### Recent Survey Responses")
        st.dataframe(
            data,
            use_container_width=True
        )
    else:
        st.info("No responses yet! Be the first to submit your dream trip.")
else:
    st.info("No survey data available yet.")
# FOOTER
st.divider()

st.markdown("""
Want to explore the results?

Navigate to the **Visuals** page using the sidebar to see:

- Population statistics from around the world
- Most popular travel destinations
- Interactive travel survey visualizations
- Average trip duration statistics
""")
