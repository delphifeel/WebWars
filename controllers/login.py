from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_user
from database import APP
from forms.login_form import LoginForm


@APP.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
