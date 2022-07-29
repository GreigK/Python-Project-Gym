from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository


activitys_blueprint = Blueprint("activitys", __name__)

@activitys_blueprint.route("/activitys")
def activitys():
    activitys = activity_repository.select_all() 
    return render_template("activitys/index.html", activitys = activitys)

@activitys_blueprint.route("/activitys/<id>")
def show(id):
    activity = activity_repository.select(id)
    members = activity_repository.members(id)
    return render_template("locations/show.html", activity=activity, members=members)