from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

connection = psycopg2.connect(
    host="localhost",
    database="test_todos",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    port="5432"
)
# import psycopg2
# #Connect to the PostgreSQL database
# connection = psycopg2.connect(
#     host="localhost",
#     database="test_todos",
#     user="postgres",
#     password="Nnaemezie21.",
#     port="5432"
# )
#print("Connected Successfully!")

#create a cursor object to interact with the database
cursor = connection.cursor()
#Create a table to store tasks
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos(
    id SERIAL PRIMARY KEY,
    task VARCHAR(100) NOT NULL,
    completed BOOLEAN DEFAULT FALSE)
""")
    connection.commit()

#print("Table Created Successfully")

def add_task(task):
    # Insert task into Postgre
    cursor.execute(
        "INSERT INTO todos(task) VALUES(%s)",
        (task,)
    )
    connection.commit()


#Read all tasks from the database
def view_tasks():
    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()
    return tasks


#Update a task in the database
def update_task(task_id):
    cursor.execute("""
    UPDATE todos
    SET completed = TRUE
    WHERE id = %s
    """, (task_id,))
    connection.commit()

#Delete a task from the database
def delete_task(task_id):
    # Delete task from PostgreSQL
    cursor.execute("""
    DELETE FROM todos
    WHERE id = %s
    """, (task_id,))
    connection.commit()


def main():
    while True:
        print("\n===== MY TO-DO APPLICATION =====")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            task = input("Enter your task: ")
            add_task(task)

        elif choice == "2":
            tasks = view_tasks()

            for task in tasks:
                print(task)

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            update_task(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)

        elif choice == "5":
            print("Thank you for using the To-Do App!")
            break

        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    create_table()
    main()


#Close the cursor and connection
cursor.close()
connection.close()