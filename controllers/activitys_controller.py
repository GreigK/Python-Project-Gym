from flask import Blueprint, Flask, redirect, render_template, request

from models.activity import Activity
import repositories.activity_repository as activity_repository
import repositories.activity_type_repository as activity_type_repository

activitys_blueprint = Blueprint("activitys", __name__)


@activitys_blueprint.route("/activitys")
def activitys():
    activitys = activity_repository.select_all()
    return render_template("activitys/index.html", activitys=activitys)



@activitys_blueprint.route("/activitys/<id>")
def show_activity(id):
    events = activity_repository.select_events_of_activity(id)
    activitys = activity_repository.select(id)
    return render_template("activitys/show.html", events=events, activitys=activitys)



@activitys_blueprint.route("/activitys/new")
def new_activity():
    activity_types = activity_type_repository.select_all()
    return render_template("activitys/new.html", activity_types=activity_types)



@activitys_blueprint.route("/activitys", methods=["POST"])
def create_activity():
    name = request.form["name"]
    activity_type_id = request.form["activity_type_id"]
    activity_type = activity_type_repository.select(activity_type_id)
    new_activity = Activity(name, activity_type)
    activity_repository.save(new_activity)
    return redirect("/activitys")



@activitys_blueprint.route("/activitys/<id>/edit")
def edit_activity(id):
    activity = activity_repository.select(id)
    activity_types = activity_type_repository.select_all()
    return render_template('activitys/edit.html', activity=activity, activity_types=activity_types)



@activitys_blueprint.route("/activitys/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    activity_type_id = request.form["activity_type_id"]
    activity_type = activity_type_repository.select(activity_type_id)
    activity = Activity(name, activity_type, id)
    activity_repository.update(activity)
    return redirect("/activitys")



@activitys_blueprint.route("/activitys/<id>/delete", methods=["POST"])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect("/activitys")
