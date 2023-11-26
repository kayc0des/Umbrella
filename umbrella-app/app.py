from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
# from model.basemodel import User, Property
# from model.persisting import session as db_session

from basemodel import User, Property, Admin
from persisting import session as db_session

app = Flask(__name__)

#randomly generated separet key using os.urandom(24)
app.secret_key = b"\xc7\xd3\xe8\xee\x95\x17\xe6\xea\t\x0c\xb9C\x92\xb4D\x16\xff#\xe8\xad\xea}AA"

bcrypt = Bcrypt(app)

def configure_views(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/admin')
    def admin():
        return render_template('adminlogin.html')
    
    @app.route('/adminpanel')
    def adminpanel():
        return render_template('admin.html')
    
    @app.route('/addproperty')
    def addproperty():
        return render_template('addproperty.html')

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
        password = request.form.get('password')

        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a User instance
        user = User(username=f"{first_name} {last_name}", email=email, password=hashed_password)

        # Save the user to the database
        db_session.add(user)
        db_session.commit()

        # Store user information in session
        session['user_id'] = user.id
        session['username'] = user.username

        # Redirect to the 'index' endpoint after form submission
        return redirect(url_for('index'))
    
    @app.route('/add_property', methods=['POST'])
    def add_property():
        # Get data from the form
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        fractions = request.form.get('fractions')
        status = request.form.get('status')
        images = request.form.get('images')

        new_property = Property(name=name, description=description, price=price, fractions=fractions,
                            status=status, images=images)
        
        new_property.fraction_price()

        # Save the property to the database
        db_session.add(new_property)
        db_session.commit()

        # Redirect to the 'index' endpoint after form submission
        return redirect(url_for('addproperty'))

    
    @app.route('/signin', methods=['POST'])
    def signin():
        # Get data from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the database to find the user by email
        user = db_session.query(User).filter_by(email=email).first()

        # Check if the user exists and the password is correct
        if user and bcrypt.check_password_hash(user.password, password):
            # Set user-related information in the session
            session['user_id'] = user.id
            session['username'] = user.username

            # Redirect to the desired page after login (e.g., user's portfolio)
            return redirect(url_for('index'))
        else:
            # Handle incorrect login credentials (e.g., show an error message)
            return render_template('login.html', error='Invalid email or password')
        
    @app.route('/admin', methods=['POST'])
    def adminlogin():
        # Get data from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the database to find the user by email
        admin = db_session.query(Admin).filter_by(email=email, password=password).first()

        # Check if the user exists and the password is correct
        if admin:
            # Set user-related information in the session
            session['user_id'] = admin.id
            session['username'] = admin.username

            # Redirect to the desired page after login (e.g., user's portfolio)
            return redirect(url_for('adminpanel'))
        else:
            # Handle incorrect login credentials (e.g., show an error message)
            return render_template('adminlogin.html', error='Invalid email or password')
    
configure_views(app)
    

if __name__ == '__main__': # ensures the script is executed directly and not when imported as a module
    app.run(host='0.0.0.0', port=8080) #listen on all available network interfaces and on port 8080