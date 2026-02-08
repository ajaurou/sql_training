import os

import duckdb

print("data" in os.listdir("./"))

conn = duckdb.connect("data/exercices_sql_tables.duckdb", read_only=True)
test = conn.execute("SELECT * FROM memory_state").df()
print(test)
