
from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member

def save(activity):
    sql = "INSERT INTO activitys(name, type) VALUES ( %s, %s ) RETURNING id"
    values = [activity.name, activity.type]
    results = run_sql(sql, values)
    activity.id = results[0]['id']
    return activity

def select_all():
    activitys = []
    
    sql = "SELECT * FROM activitys"
    results = run_sql(sql)

    for row in results:
        activity = Activity(row['name'], row['type'], row['id'])
        activitys.append(activity)
    return activitys


def select(id):
    activity = None
    sql = "SELECT * FROM activitys WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity(result['name'], result['type'], result['id'])
    return activity


def delete_all():
    sql = "DELETE FROM activitys"
    run_sql(sql)


def members(id):
    sql = "SELECT members.* FROM members INNER JOIN booking ON member.id WHERE bookings.activity_id = %s"
    values = [id]
    results = run_sql(sql, values)

    members = []
    for row in results:
        member = Member(row["name"], row["id"])
        members.append(member)
    return members