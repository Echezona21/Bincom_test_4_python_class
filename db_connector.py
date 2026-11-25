import psycopg2
#Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="test_todos",
    user="postgres",
    password="password",
    port="5432"
)
#print("Connected Successfully!")