import psycopg2
#Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="test_todos",
    user="postgres",
    password="Nnaemezie21.",
    port="5432"
)

print("Connected Successfully!")
#create a cursor object to interact with the database
cursor = connection.cursor()
#Create a table to store tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
    id SERIAL PRIMARY KEY,
    task VARCHAR(100),
    completed BOOLEAN DEFAULT FALSE
)
""")

connection.commit()

print("Table Created Successfully")

#Create a list of tasks to add to the database
tasks = [
    "Take Bincom Test",
    "Revise PostgreSQL",
    "Revise Python",
    "Practice CRUD",
    "Learn Functions",
    "Study APIs",
    "Revise Algorithms",
    "Drink A Bottle of Beer",
    "Search for Jobs",
    "Cook Dinner"
]
#print("Adding 10 Tasks to the Database...")

for task in tasks:
    cursor.execute(
        "INSERT INTO tasks(task_name) VALUES(%s)",
        (task,)
    )

connection.commit()

print("10 Tasks Added Successfully")