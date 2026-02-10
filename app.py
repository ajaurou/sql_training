import logging
import os
import subprocess
import sys

import duckdb
import streamlit as st

app_logger = st.logger.get_logger(__name__)
app_logger.setLevel(logging.INFO)  # ici on peut mettre DEBUG, ERROR, WARNING


if "data" not in os.listdir("./"):
    app_logger.info(os.listdir("./"))
    app_logger.info("Creating data folder")
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("./data/"):
    app_logger.info(os.listdir("./data/"))
    app_logger.info("init_db.py is running to create the database")
    subprocess.run([sys.executable, "init_db.py"], capture_output=True, text=True)
    app_logger.info("Database created")

conn = duckdb.connect("data/exercices_sql_tables.duckdb", read_only=False)


st.write("""
# SQL SRS
Spaced Repetition SQL practice""")


with st.sidebar:
    themes_df = conn.execute("select distinct theme from memory_state").df()
    themes_list = themes_df["theme"].tolist()
    theme = st.selectbox(
        "What would you like to review?",
        themes_list,
        placeholder="Select a theme",
    )

    if theme:
        exercices = (
            conn.execute(f"select * from memory_state where theme = '{theme}'")
            .df()
            .sort_values("last_reviewed")
            .reset_index(drop=True)
        )
        st.write(exercices)
    else:
        exercices = (
            conn.execute("select * from memory_state")
            .df()
            .sort_values("last_reviewed")
            .reset_index(drop=True)
        )

    exercice_name = exercices.loc[0, "exercice_name"]
    with open(f"data/solutions/{exercice_name}.sql") as file:
        query_solution = file.read()

    solution_df = conn.execute(query_solution).df()


st.header("Enter your code:")
query = st.text_area(label="Your SQL code here", key="user_input")

if query:
    result = conn.execute(query).df()
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

with tab3:
    st.write(f"Answer: {query_solution}")
