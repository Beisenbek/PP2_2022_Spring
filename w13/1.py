import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=bsnbk password=password")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM students")

# Retrieve query results
records = cur.fetchall()

print(records)