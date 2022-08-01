from ssl import MemoryBIO
from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, premium) VALUES (%s, %s) RETURNING id"
    values = [member.name, member.premium]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id


def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result['premium'] ,result["id"])
        members.append(member)
    return members


def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result["name"], result['premium'] ,result["id"])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(member):
    sql = "UPDATE members SET (name, premium) = (%s, %s) WHERE id = %s"
    values = [member.name, member.premium ,member.id]
    run_sql(sql, values)