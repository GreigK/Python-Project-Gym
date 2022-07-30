from flask import Blueprint, Flask, redirect, render_template, request

from models.activity_type import ActivityType
import repositories.activity_type_repository as activity_type_repository

activity_type_blueprint = Blueprint("activity_type", __name__)


@activity_type_blueprint.route("/activitytypes")
def activity_type():
    activity_type = activity_type_repository.select_all()
    return render_template("activity_types/index.html", activity_type=activity_type)



@activity_type_blueprint.route("/activitytypes/new")
def new_activity_type():
    return render_template("activity_types/new.html")



@activity_type_blueprint.route("/activitytypes", methods=["POST"])
def create_activity_type():
    name = request.form["name"]
    new_activity_type = ActivityType(name)
    activity_type_repository.save(new_activity_type)
    return redirect("/activitytypes")



@activity_type_blueprint.route("/activitytypes/<id>/edit")
def edit_activity_type(id):
    activity_type = activity_type_repository.select(id)
    return render_template('activity_type/edit.html', activity_type=activity_type)



@activity_type_blueprint.route("/activitytype/<id>", methods=["POST"])
def update_activity(id):
    name = request.form["name"]
    activity_type = ActivityType(name, id)
    activity_type_repository.update(activity_type)



@activity_type_blueprint.route("/activitytypes/<id>/delete", methods=["POST"])
def delete_activity(id):
    activity_type_repository.delete(id)
    return redirect("/activitytypes")