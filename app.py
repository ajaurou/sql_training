import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))


CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))


st.write("""
# SQL SRS
Spaced Repetition SQL practice""")


with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "Aggregation", "Windows function"),
        placeholder="Select a theme",
    )


solution_str = """
    select * from beverages
    cross join food_items"""

solution_df = duckdb.query(solution_str).df()

st.header("Enter your code:")
query = st.text_area(label="Your SQL code here", key="user_input")
if query:
    result = duckdb.query(query).df()
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Your code does not have the right number of columns")
    else:
        st.write("Your code has the right number of columns")

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        print(f"{e} - Columns naming is incorrect")


tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    st.write("Table: beverages")
    st.dataframe(beverages)
    st.write("Table: food_items")
    st.dataframe(food_items)
    st.write("Expected:")
    st.dataframe(solution_df)

with tab3:
    st.write(f"Answer: {solution_str}")
