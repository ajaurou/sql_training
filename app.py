import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQL SRS
Spaced Repetition SQL practice""")


option = st.selectbox(
    "What would you like to review?",
    ("Joins", "Aggregation", "Windows function"),
    placeholder='Select a theme'
)

st.write("You selected:", option)

data = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
}

df = pd.DataFrame(data)

tab1, tab2 = st.tabs(['SQL', 'Python'])

with tab1:
    sql_query = st.text_area("Type your SQL query")
    st.write(f'Your SQL query {sql_query}')
    st.dataframe(duckdb.sql(sql_query))
