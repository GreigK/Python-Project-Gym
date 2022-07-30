from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)



@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    activitys = activity_repository.select_all()
    return render_template("bookings/new.html", members=members, activitys=activitys)



@bookings_blueprint.route("/bookings", methods=["POST"])
def create_bookings():
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    new_booking = Booking(member, activity)
    booking_repository.save(new_booking)
    return redirect("/bookings")



@bookings_blueprint.route("/bookings/<id>/edit")
def edit_bookings(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    activitys = activity_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, activitys=activitys)



@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    booking = Booking(member, activity, id)
    booking_repository.update(booking)
    return redirect("/bookings")



@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")