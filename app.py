'''
Importing the necessary libraries/components, etc. to make the code run.
    -Flask
    -SQLAlchemy
'''
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


'''
__authors__ = ['Jenna Purdy']
__date__ = 20220515
__description__ = "Movie list app for CICD (Continuous Integration, Continuous Development)"
'''


'''
Creating a Flask instance for the app

Python sets the __name__ variable to the module name. For example, in a module named test.py that is located in the top-level directory of the application, the value of __name__ is "test". If the test.py module is located inside a Python package called my_package, then the value of __name__ is "my_package.test".

The first argument to the Flask class is called import_name (the name of the application package. Usually, the Flask instance is created by passing __name__ for this argument.)

More Info: https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class
'''
app = Flask(__name__)

'''
Applications require configuration in order to run. This first two lines of code are modifying two configuration settings for the application: the first attaches itself to a database and the second sets the database tracking of modifications to false, so that it won't track changes.
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


'''
Creating Movie class to use as the database Model. 

The function db.Column() takes parameters to set the variable type.
Every item added to the database must have three attributes: id, title, and complete. 
The id will be an integer automatically assigned by the database to be used as the primary key. 
The title is a string with up to 100 characters. 
And complete is a boolean variable.
'''
class Movie(db.Model):
    """A dummy docstring."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


'''
Establishing the default route for the landing page, identifying which template to render for the page, and passing the necessary argument for the page to render correctly.
'''
@app.route("/")
def list1():
    """A dummy docstring"""
    movie_list = Movie.query.all()
    return render_template("list.html", movie_list=movie_list)


'''
Establishing the home route, identifying which template to render for the page, and passing the necessary argument for the page to render correctly.
'''
@app.route("/edit")
def home():
    """A dummy docstring"""
    movie_list = Movie.query.all()
    return render_template("base.html", movie_list=movie_list)


'''
Establishing the add route to post a new item to the database. Line 78 creates the variable title and uses response.form.get() to pull the value from the input box on the form and assigns it to the variable. Then new_movie creates the object based on the Movie class and sets the properties. Next, db.session.add() adds the new item to the database. session.commit() is used to commit the current transaction. Finally, the user is "redirected" back to the same page (and not to the /add url)
'''
@app.route("/add", methods=["POST"])
def add():
    """A dummy docstring"""
    title = request.form.get("title")
    new_movie = Movie(title=title, complete=False)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:movie_id>")
def update(movie_id):
    """A dummy docstring"""
    movie = Movie.query.filter_by(id=movie_id).first()
    movie.complete = not movie.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    """A dummy docstring"""
    movie = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    app.run()