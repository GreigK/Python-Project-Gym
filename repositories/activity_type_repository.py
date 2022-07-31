from db.run_sql import run_sql
from models.activity_type import ActivityType

def save(activity_type):
    sql = "INSERT INTO activity_types (name) VALUES (%s) RETURNING id"
    values = [activity_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity_type.id = id


def select_all():
    activity_types = []
    sql = "SELECT * FROM activity_types"
    results = run_sql(sql)
    for result in results:
        activity_type = ActivityType(result["name"], result["id"])
        activity_types.append(activity_type)
    return activity_types


def select(id):
    activity_type = None 
    sql = "SELECT * FROM activity_types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        activity_type = ActivityType(result["name"], result["id"])
    return activity_type


def delete_all():
    sql = "DELETE FROM activity_types"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM activity_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(activity_type):
    sql = "UPDATE activity_types SET name = %s WHERE id = %s"
    values = [activity_type.name, activity_type.id]
    run_sql(sql, values)