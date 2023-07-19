from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "kosta"
password = "123"
facebook_friends=["Joelle" , "Jawad" , "Mom" , "Dad" , "Kosta" , "Kenda" , "Rani"]


@app.route('/' , methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else : 
		if username == request.form['username'] and password == request.form['password'] :
			return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('home.html' , flist = facebook_friends)
 
@app.route('/friend_exists/<string:name>' , methods=['GET','POST'])
def friendsexist(name):
	b = False
	for i in facebook_friends:
		if i == name:
			b = True
			return render_template('friend_exists.html' , bool=b , n=name)
	return render_template('friend_exists.html' , bool=b , n=name)



  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
