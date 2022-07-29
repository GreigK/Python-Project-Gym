from flask import Flask, render_template

from controllers.booking_controller import bookings_blueprint
from controllers.member_controller import members_blueprint
from controllers.activity_controller import activitys_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(activitys_blueprint)

@app.route('/')
def home():
    return render_template('index.html')