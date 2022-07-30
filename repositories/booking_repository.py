from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
from models.activity import Activity
import repositories.activity_repository as activity_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.activity.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        activity = activity_repository.select(result["activity_id"])
        booking = Booking(member, activity, result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    booking = None 
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]

    results = run_sql(sql, values)


    if results:
        result = results[0]
        member = member_repository.select(result["member_id"])
        activity = activity_repository.select(result["activity_id"])
        booking = Booking(member, activity, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (member_id, activity_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.activity.id, booking.id]
    run_sql(sql, values)

