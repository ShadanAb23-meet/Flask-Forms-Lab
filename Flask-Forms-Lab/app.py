from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)



username = "berreisandcream"
password = "2332004"
facebook_friends=["mina","zena","eden", "raghad", "mohammed", "yasmin"]


@app.route('/', methods=["GET", "POST"])  # '/' for the default page
def login():
		if request.method=="GET":
				return render_template('login.html')
		else:
				return.redirect(url_for("login"))



	@app.route("/home")
	def home():
		return.render_template("home.html", facebook_friends=facebook_friends)

	@app.route('/friends/<string:name>',methods=["GET","POST"])
	def friends(name):
		if name in facebook_friends
		 exist= True
		 return render_template("facebook_friends.html",exist=exist)
		else:
			exist=False
			return render_template("facebook_friends.html",n=name, exist=exist)  	  		



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)