import sqlite3


conn = sqlite3.connect(
    "nifty100.db"
)


with open(
    "notebooks/review.sql"
) as f:

    queries = f.read().split(";")



for q in queries:

    if q.strip():

        print("\n----------------")
        print(q)

        result = conn.execute(q).fetchall()

        for row in result:
            print(row)



conn.close()
