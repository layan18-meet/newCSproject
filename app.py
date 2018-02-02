from flask import Flask, flash, redirect, render_template, request, Session, abort
import os
from flask_sqlalchemy import SQLAlchemy 
#from flask.ext.login import LoginManager, login_user, current_user, login_required, logout_user
# from flask.ext.session import Session

app= Flask(__name__)
app.debug=True
app.config ['SQLALCHEMY_DATABASE_URI']= 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db= SQLAlchemy(app)
# sess= Session()

class User (db.Model):
	id= db.Column(db.Integer, primary_key= True, autoincrement=True)
	name= db.Column(db.String(80), nullable= False)
	password= db.Column(db.String(80), nullable= False)

	
db.create_all()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/articles')
def articles():
	return render_template("articles.html")

@app.route('/info/antibiotics')
def antibiotics():
	return render_template("antibiotics.html")

@app.route('/info/painkillers')
def painkillers():
	return render_template("painkillers.html")

@app.route('/info/WhyChange')
def whychng():
	return render_template("whychng.html")

@app.route('/personalStories')
def personal_stories():
	return render_template("personal_stories.html")

@app.route('/alternatives')
def alternatives():
	return render_template("alternatives.html")

@app.route('/debate')
def debate():
	return render_template("debate.html")

@app.route('/signIn')
def sign_in():
	return render_template("sign_in.html")

@app.route('/signUp')
def sign_up():
	return render_template("sign_up.html")


@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		user = User()
		user.name = request.form['username']
		user.password = request.form['password']
		db.session.add(user)
		db.session.commit()
		return render_template('index.html' , user=user)
	else:
		return render_template("sign_up.html")

if __name__== '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] 	= 'filesystem'
	# sess.init_app(app)
	app.run(debug=True)


@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return redirect(next or url_for('index'))
    return render_template('sign_in.html', form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect('index.html')

#!/usr/bin/python
#flask-login anonymous user class
from flask.ext.login import AnonymousUserMixin
class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'