import streamlit as st
import pandas as pd
import duckdb
import io

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''
beverages = pd.read_csv(io.StringIO(csv))


csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''
food_items = pd.read_csv(io.StringIO(csv2))


st.write("""
# SQL SRS
Spaced Repetition SQL practice""")


with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "Aggregation", "Windows function"),
        placeholder='Select a theme'
    )



answer = """
    select * from beverages
    cross join food_items"""

solution = duckdb.query(answer).df()

st.header('Enter your code:')
query = st.text_area(label='Your SQL code here', key='user_input')
if query:
    result = duckdb.query(query).df()
    st.dataframe(result)


tab2, tab3 = st.tabs(['Tables', 'Solutions'])

with tab2:
    st.write('Table: beverages')
    st.dataframe(beverages)
    st.write('Table: food_items')
    st.dataframe(food_items)
    st.write('Expected:')
    st.dataframe(solution)

with tab3:
    st.write(f'Answer: {answer}')
