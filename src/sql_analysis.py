import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/sales.db"
)

query = """
SELECT
    Region,
    ROUND(SUM(Sales),2) AS Revenue
FROM sales
GROUP BY Region
ORDER BY Revenue DESC
"""

result = pd.read_sql(
    query,
    conn
)

print(result)

conn.close()