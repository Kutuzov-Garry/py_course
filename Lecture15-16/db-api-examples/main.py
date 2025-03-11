# Igor, for DB-API sqlite3.

import sqlite3

conn = sqlite3.connect("todo.db")
print(type(conn))  # <class 'sqlite3.Connection'>.

c = conn.cursor()
print(type(c))  # <class 'sqlite3.Cursor'>.

# create table.
# c.execute("""CREATE TABLE IF NOT EXISTS tasks (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );""")

# insert.
# c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))

# conn.commit()

# insert many.
# create list with tuples of data.
# tasks = [
#    ("My new task", 15),
#    ("My second task", 5),
#    ("My third task", 10),
#]

# c.executemany("INSERT INTO tasks (name, priority) VALUES (?,?)", tasks)
# conn.commit()

# select all.
# for row in c.execute("SELECT * FROM tasks"):
#    print(row)

# select all and fetch all.
# c.execute("SELECT * FROM tasks")

# rows = c.fetchall()

# for row in rows:
#    print(row)

# select all and fetch one.
# c.execute("SELECT * FROM tasks")

# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)

# update id-1 с приоритетом-20.
# c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (20, 1))
# conn.commit()

# delete id-1.
# c.execute("DELETE FROM tasks WHERE id = ?", (1,))
# conn.commit()

# close connection.
# conn.close()

# the better way - example.
# with sqlite3.connect("todo.db") as conn:
#     with conn.cursor() as c:
#         c.execute("""CREATE TABLE IF NOT EXISTS tasks (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         priority INTEGER NOT NULL
#         );""")
#
#     c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))
#
#     conn.commit()
