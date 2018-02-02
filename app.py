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

@app.route('/home')
def index2():
	return render_template("index2.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/About')
def about_before():
	return render_template("about_before.html")

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

@app.route('/sign_in')
def sign_in():
	return render_template("sign_in.html")

@app.route('/sign_up')
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

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
	if request.method == "GET":
		return render_template('sign_in.html')
	elif request.method == "POST":
		log_in = User.query.filter_by(user=request.form['name'], password=request.form['password']).first()
	if log_in == None:
		return render_template('sign_in.html', log_in=False)
	else:
		return render_template('index2.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect('index.html')





if __name__== '__main__':
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] 	= 'filesystem'
	# sess.init_app(app)
	app.run(debug=True)