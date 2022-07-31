from db.run_sql import run_sql
from models.member import Member
from models.activity import Activity
from models.activity_type import ActivityType
import repositories.activity_type_repository as activity_type_repository 

def save(activity):
    sql = "INSERT INTO activitys (name, activity_types_id) VALUES (%s, %s) RETURNING id"
    values = [activity.name, activity.activity_types.id]
    results = run_sql(sql, values)
    activity.id = results[0]['id']
    


def select_all():
    activitys = []
    sql = "SELECT * FROM activitys"
    results = run_sql(sql)
    for result in results:
        activity_type = activity_type_repository.select(result["activity_type_id"])
        activity = Activity(result["name"], activity_type, result["id"])
        activitys.append(activity)
    return activitys


def select(id):
    sql = "SELECT * FROM activitys WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    
    if results:
        result = results[0]
        activity_type = activity_type_repository.select(result["activity_type_id"])
        activity = Activity(result["name"], activity_type, result["id"])
    return activity


def delete_all():
    sql = "DELETE FROM activitys"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM activitys WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(activity):
    sql = "UPDATE activitys SET (name, activity_type_id) = (%s, %s) WHERE id = %s"
    values = [activity.name, activity.activity_type.id, activity.id]
    run_sql(sql, values)


def select_events_of_activity(id):
    events = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = Member(result["name"])
        events.append(member)
    return events