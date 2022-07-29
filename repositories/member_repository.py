
from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member


def save(member):
    sql = "INSERT INTO members( name ) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql( sql, values )
    member.id = results[0]['id']

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def activity(id):
    sql = "SELECT activitys.* FROM activitys INNER JOIN bookings ON activitys.id = bookings.activity_id WHERE bookings.member_id = %s"
    values =[id]
    results = run_sql(sql, values)

    activitys = []
    for row in results:
        activity = Activity(row["name"],row["type"],row["id"])
        activitys.append(activity)
    return activitys