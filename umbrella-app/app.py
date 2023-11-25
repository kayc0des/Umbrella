from flask import Flask, render_template, request, redirect, url_for
from basemodel import User
from persisting import session

app = Flask(__name__)

def configure_views(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/submit_user', methods=['POST'])
    def submit_user():
        # Get data from the form
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        # Create a User instance
        user = User(username=f"{first_name} {last_name}", email=email)

        # Save the user to the database
        session.add(user)
        session.commit()

        # Redirect to the 'index' endpoint after form submission
        return redirect(url_for('index'))
    
configure_views(app)
    

if __name__ == '__main__': # ensures the script is executed directly and not when imported as a module
    app.run(host='0.0.0.0', port=8080) #listen on all available network interfaces and on port 8080