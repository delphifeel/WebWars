from flask import render_template
from flask.ext.login import login_required
from database import APP


@APP.route('/')
@login_required
def index():
    return render_template('index.html')