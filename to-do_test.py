import psycopg2
#Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="test_todos",
    user="postgres",
    password="Nnaemezie21.",
    port="5432"
)
#print("Connected Successfully!")

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

#print("Table Created Successfully")

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
        "INSERT INTO todos(task) VALUES(%s)",
        (task,)
    )

connection.commit()
#print("10 Tasks Added Successfully")

#Read all tasks from the database
cursor.execute("SELECT * FROM todos")
tasks = cursor.fetchall()
for task in tasks:
    print(task)

#Update a task in the database
cursor.execute("""
UPDATE todos
SET completed = TRUE
WHERE id = %s
""", (1,))

connection.commit()

#Delete a task from the database
cursor.execute("""
DELETE FROM todos
WHERE id = %s
""", (2,))
connection.commit()

#Close the cursor and connection
cursor.close()
connection.close()