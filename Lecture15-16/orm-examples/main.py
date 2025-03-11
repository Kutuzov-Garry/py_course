# Igor, for ORM peewee.

import peewee
import datetime

db = peewee.SqliteDatabase("todo.db")

class Task(peewee.Model):
    task_name = peewee.CharField()
    task_priority = peewee.IntegerField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = "tasks"


Task.create_table()

note1 = Task.create(task_name="Went to the cinema", task_priority=10)
note1.save

note2 = Task.create(task_name="Exercised in the morning", task_priority=11)
note2.save

note3 = Task.create(task_name="Worked in the garden", task_priority=4)
note3.save

note4 = Task.create(task_name="Listened to music", task_priority=66)
note4.save
