import duckdb
import streamlit as st

conn = duckdb.connect("data/exercices_sql_tables.duckdb", read_only=False)


st.write("""
# SQL SRS
Spaced Repetition SQL practice""")


with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "Joins", "Aggregation", "Windows function"),
        placeholder="Select a theme",
    )

    exercices = conn.execute(f"select * from memory_state where theme = '{theme}'").df()
    st.write(exercices)

# SOLUTION_STR = """
#     select * from beverages
#     cross join food_items"""

# solution_df = duckdb.query(SOLUTION_STR).df()

st.header("Enter your code:")
query = st.text_area(label="Your SQL code here", key="user_input")

if query:
    result = conn.execute(query).df()
    st.dataframe(result)

#     if len(result.columns) != len(solution_df.columns):
#         st.write("Your code does not have the right number of columns")
#     else:
#         st.write("Your code has the right number of columns")

#     try:
#         result = result[solution_df.columns]
#         st.dataframe(result.compare(solution_df))
#     except KeyError as e:
#         print(f"{e} - Columns naming is incorrect")


tab2, tab3 = st.tabs(["Tables", "Solutions"])

with tab2:
    st.write(exercices.loc[0, "tables"])
    exercices_tables = exercices.loc[0, "tables"]
    for table in exercices_tables:
        st.write(f"Table: {table}")
        st.dataframe(conn.execute(f"select * from {table}").df())

#     st.write("Table: beverages")
#     st.dataframe(beverages)
#     st.write("Table: food_items")
#     st.dataframe(food_items)
#     st.write("Expected:")
#     st.dataframe(solution_df)

# with tab3:
#     st.write(f"Answer: {SOLUTION_STR}")
