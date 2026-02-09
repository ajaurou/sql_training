import os

import duckdb

print("data" in os.listdir("./"))

conn = duckdb.connect("data/exercices_sql_tables.duckdb", read_only=True)
exercices = conn.execute("SELECT * FROM memory_state").df()
exercices_tables = exercices.loc[0, "tables"]
print(exercices_tables)
