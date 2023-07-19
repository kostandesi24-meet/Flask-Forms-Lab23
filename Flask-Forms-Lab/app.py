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
users = {"kosta":"123" , "joelle":"1234" , "george":"kosta"}



@app.route('/' , methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	if request.form['username'] in users :
		if users[request.form['username']] == request.form['password']:
			return redirect(url_for('home'))
	return render_template('login.html' , wrong = "The UserName or the Password is wrong !")

	# else : 
	# 	if username == request.form['username'] and password == request.form['password'] :
	# 		return redirect(url_for('home'))
	# 	else:
	# 		return render_template('login.html' , wrong = "The UserName or the Password is wrong !")

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
