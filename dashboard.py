import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Analytics Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview:")
    st.write(df.head())

    st.write("### Data Statistics:")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(['number']).columns
    column = st.selectbox("Select a column to visualize", numeric_columns)

    if column:
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

