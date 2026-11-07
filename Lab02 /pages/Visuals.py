import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.title("Data Visualizations")

st.header("Part 1: Population Data")

with open("data.json", "r") as file:
    json_data = json.load(file)

countries = []
populations = []

for item in json_data["data_points"]:
    countries.append(item["label"])
    populations.append(item["value"])


st.subheader("Chart 1: Population by Country")

fig1, ax1 = plt.subplots()

ax1.bar(countries, populations)

ax1.set_title("Population by Country")
ax1.set_xlabel("Country")
ax1.set_ylabel("Population (Millions)")

plt.setp(ax1.get_xticklabels(), rotation=45, ha="right")

fig1.tight_layout()

st.pyplot(fig1)
plt.close(fig1)


st.subheader("Chart 2: Interactive Population Distribution")

st.write("Use the slider to select how many countries to display.")


if "country_count" not in st.session_state:
    st.session_state.country_count = 5

st.slider(
    "Number of countries",
    min_value=2,
    max_value=len(countries),
    key="country_count"
)


selected_countries = countries[:st.session_state.country_count]
selected_populations = populations[:st.session_state.country_count]

fig2, ax2 = plt.subplots()

ax2.pie(
    selected_populations,
    labels=selected_countries,
    autopct="%1.1f%%"
)

ax2.set_title("Population Distribution")

st.pyplot(fig2)
plt.close(fig2)


# EXTRA CREDIT: 

st.write("Population Statistics")

json_mean = pd.Series(selected_populations).mean()
json_median = pd.Series(selected_populations).median()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Mean Population (Millions)",
        value=round(json_mean, 2)
    )

with col2:
    st.metric(
        label="Median Population (Millions)",
        value=round(json_median, 2)
    )

st.header("Part 2: Survey Data")


st.header("Part 2: Survey Data")

csv_data = pd.read_csv("data.csv")

csv_data["Value"] = pd.to_numeric(
    csv_data["Value"],
    errors="coerce"
)

csv_data = csv_data.dropna(subset=["Value"])

if not csv_data.empty:

    st.subheader("Chart 3: Survey Results")

    fig3, ax3 = plt.subplots()

    ax3.bar(
        csv_data["Category"],
        csv_data["Value"]
    )

    ax3.set_title("Survey Results by Category")
    ax3.set_xlabel("Category")
    ax3.set_ylabel("Value")

    plt.setp(ax3.get_xticklabels(), rotation=45, ha="right")

    fig3.tight_layout()

    st.pyplot(fig3)
    plt.close(fig3)

    st.subheader("Chart 4: Interactive Survey Results")

    st.write("Use the slider to select how many survey responses to display.")

    if "survey_count" not in st.session_state:
        st.session_state.survey_count = len(csv_data)

    if st.session_state.survey_count > len(csv_data):
        st.session_state.survey_count = len(csv_data)

    if len(csv_data) > 1:

        st.slider(
            "Number of survey responses",
            min_value=1,
            max_value=len(csv_data),
            key="survey_count"
        )

    else:
        st.session_state.survey_count = 1
        st.info("Submit more survey responses to use the interactive slider!")

    selected_data = csv_data.head(st.session_state.survey_count)

    fig4, ax4 = plt.subplots()

    ax4.scatter(
        selected_data["Category"],
        selected_data["Value"]
    )

    ax4.set_title("Interactive Survey Results")
    ax4.set_xlabel("Category")
    ax4.set_ylabel("Value")

    plt.setp(ax4.get_xticklabels(), rotation=45, ha="right")

    fig4.tight_layout()

    st.pyplot(fig4)
    plt.close(fig4)

    # EXTRA CREDIT
    st.write("Survey Statistics")

    csv_mean = selected_data["Value"].mean()
    csv_median = selected_data["Value"].median()
    col3, col4 = st.columns(2)
    with col3:
        st.metric(
            label="Mean Survey Value",
            value=round(csv_mean, 2)
        )
    with col4:
        st.metric(
            label="Median Survey Value",
            value=round(csv_median, 2)
        )
else:
    st.info("No survey responses have been submitted yet.")
