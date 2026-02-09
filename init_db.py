import io
import os

import duckdb
import pandas as pd

if "data" not in os.listdir("./"):
    os.mkdir("data")

if "exercices_sql_tables.duckdb" in os.listdir("./data/"):
    os.remove("data/exercices_sql_tables.duckdb")

# create a connection to a file called 'file.db'
conn = duckdb.connect("data/exercices_sql_tables.duckdb", read_only=False)
# --------------------------------------------------------------------------------------
# EXERCICE LIST
# --------------------------------------------------------------------------------------
data = {
    "theme": ["cross_joins", "cross_joins"],
    "exercice_name": ["beverages_and_food", "sizes_and_trademarks"],
    "tables": [["beverages", "food_items"], ["sizes", "trademarks"]],
    "last_reviewed": ["2001-01-01", "2000-01-01"],
}

memory_state_df = pd.DataFrame(data)
conn.execute("DROP TABLE IF EXISTS memory_state")
conn.execute("CREATE TABLE memory_state AS SELECT * FROM memory_state_df")

# --------------------------------------------------------------------------------------
# CROSS JOIN EXERCICE
# --------------------------------------------------------------------------------------
CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
conn.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""
food_items = pd.read_csv(io.StringIO(CSV2))
conn.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")

sizes = """
size
XS
M
L
XL
"""
sizes = pd.read_csv(io.StringIO(sizes))
conn.execute("CREATE TABLE IF NOT EXISTS sizes AS SELECT * FROM sizes")

trademarks = """
trademark
Nike
Asphalte
Abercrombie
Lewis
"""

trademarks = pd.read_csv(io.StringIO(trademarks))
conn.execute("CREATE TABLE IF NOT EXISTS trademarks AS SELECT * FROM trademarks")
