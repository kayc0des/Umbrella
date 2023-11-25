# flask_tutorial/app.py

from flask import Flask, render_template, request, redirect, url_for
from models.persisting import session
from models.basemodel import User  # Import the User class

app = Flask(__name__)

def configure_views(app):
    @app.route('/')
    def index():
        return render_template('login.html')

    @app.route('/submit_user', methods=['POST'])
    def submit_user():
        # Get data from the form
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')


        # Create the User instance
        user = User(username=f"{first_name} {last_name}", email=email)

        # Add the user to the session
        session.add(user)

        # Commit the changes to the database
        session.commit()

        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
