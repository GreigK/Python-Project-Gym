from flask import Flask, render_template

from controllers.bookings_controller import bookings_blueprint
from controllers.member_controller import members_blueprint
from controllers.activitys_controller import activitys_blueprint
from controllers.activity_types_controller import activity_type_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(activitys_blueprint)
app.register_blueprint(activity_type_blueprint)

@app.route('/')
def home():
    return render_template('index.html')
