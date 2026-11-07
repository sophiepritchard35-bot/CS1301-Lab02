import streamlit as st

st.set_page_config(
    page_title="Global Data Dashboard",
    page_icon="🌍",
    layout="wide"
)
st.title("Global Population & Travel Dashboard")

st.write("""
Welcome to my CS 1301 Web Development Lab 2!

Explore population statistics from around the world,
share your dream travel destination, and discover
interesting trends through interactive visualizations.
""")

st.divider()
st.header("Explore the Dashboard")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Travel Survey")

    st.write("""
    Where would you like to travel?

    Visit the Survey page to:
    - Select your dream destination
    - Choose how many days you would stay
    - Submit your response to our dataset
    - View responses from other users
    """)

    if st.button("Go to Survey"):
        st.switch_page("pages/Survey.py")

with col2:
    st.subheader("📈 Data Visualizations")

    st.write("""
    Explore population statistics and travel trends!

    Visit the Visuals page to:
    - Compare populations across countries
    - Explore interactive population charts
    - Analyze travel survey responses
    - View mean and median statistics
    """)

    if st.button("Explore Visualizations"):
        st.switch_page("pages/Visuals.py")
