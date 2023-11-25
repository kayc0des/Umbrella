from flask import Flask, render_template, request, redirect, url_for, session
from basemodel import User
from persisting import session as db_session

app = Flask(__name__)

#randomly generated separet key using os.urandom(24)
app.secret_key = b"\xc7\xd3\xe8\xee\x95\x17\xe6\xea\t\x0c\xb9C\x92\xb4D\x16\xff#\xe8\xad\xea}AA"

def configure_views(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/portfolio')
    def portfolio():
        return render_template('portfolio.html')
    
    @app.route('/logout')
    def logout():
        # Clear the session data
        session.clear()
        return redirect(url_for('index'))  # Redirect to the login page after logout

    @app.route('/submit_user', methods=['POST'])
    def submit_user():
        # Get data from the form
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        # Create a User instance
        user = User(username=f"{first_name} {last_name}", email=email)

        # Save the user to the database
        db_session.add(user)
        db_session.commit()

        # Store user information in session
        session['user_id'] = user.id
        session['username'] = user.username

        # Redirect to the 'index' endpoint after form submission
        return redirect(url_for('index'))
    
configure_views(app)
    

if __name__ == '__main__': # ensures the script is executed directly and not when imported as a module
    app.run(host='0.0.0.0', port=8080) #listen on all available network interfaces and on port 8080