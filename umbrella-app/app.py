import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
# from model.basemodel import User, Property
# from model.persisting import session as db_session

from basemodel import User, Property, Admin, Message
from persisting import session as db_session

app = Flask(__name__)

#randomly generated separet key using os.urandom(24)
app.secret_key = b"\xc7\xd3\xe8\xee\x95\x17\xe6\xea\t\x0c\xb9C\x92\xb4D\x16\xff#\xe8\xad\xea}AA"

bcrypt = Bcrypt(app)

# Function to fetch all properties from the database
def get_properties():
    return db_session.query(Property).all()

def configure_views(app):
    @app.route('/')
    def index():
        properties = get_properties()
        return render_template('index.html', properties=properties)
    
    @app.route('/fetch_properties', methods=['GET'])
    def fetch_properties():
        properties = db_session.query(Property).all()
        property_list = [{
            'propertyName': property.name,
            'propertyID': property.id,
            'propertyLocation': property.location,  
            'propertyDesc': property.description,
            'propertyStatus': property.status,
            'propertyDateAdded': property.created_at
        } for property in properties]
        return jsonify(property_list)
    
    @app.route('/fetch_users', methods=['GET'])
    def fetch_users():
        users = db_session.query(User).all()
        user_list = [{
            'userName': user.username,
            'userID': user.id,
            'userEmail': user.email
        } for user in users]
        return jsonify(user_list)
    
    @app.route('/fetch_messages', methods=['GET'])
    def fetch_messages():
        messages = db_session.query(Message).all()
        message_list = [{
            'messageID': message.id,
            'userID': message.user_id,
            'messageText': message.text
        } for message in messages]
        return jsonify(message_list)

    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.route('/properties')
    def properties():
        return render_template('property.html')
    
    @app.route('/messages')
    def messages():
        return render_template('messages.html')
    
    @app.route('/admin')
    def admin():
        return render_template('adminlogin.html')
    
    @app.route('/adminpanel')
    def adminpanel():
        total_properties = db_session.query(Property).count()
        total_users = db_session.query(User).count()
        total_admins = db_session.query(Admin).count()

        return render_template('admin.html', total_properties=total_properties, total_users=total_users, total_admins=total_admins)
    
    @app.route('/addproperty')
    def addproperty():
        return render_template('addproperty.html')
    
    @app.route('/investors')
    def investors():
        return render_template('investors.html')

    @app.route('/portfolio')
    def portfolio():
        return render_template('portfolio.html')
    
    @app.route('/logout')
    def logout():
        # Clear the session data
        session.clear()
        return redirect(url_for('index'))  # Redirect to the login page after logout
    
    @app.route('/add_message', methods=['POST'])
    def add_message():
        if 'user_id' in session:
            # User is logged in
            user_id = session['user_id']
            email = request.form.get('email')
            message_text = request.form.get('message')

            # Assuming you have a function to add a message to the database
            message = Message(user_id=user_id, text=message_text)

            db_session.add(message)
            db_session.commit()

            # Redirect or do any other necessary actions
            return redirect(url_for('contact'))
        else:
            # User is not logged in, handle accordingly
            return redirect(url_for('contact'))

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
        location = request.form.get('location')
        price = request.form.get('price')
        fractions = request.form.get('fractions')
        status = request.form.get('status')
        # images = request.form.get('images')

        property_image = request.files['images']
        if property_image.filename != '':
            image_filename = secure_filename(property_image.filename)
            image_path = os.path.join(app.static_folder, 'assets', 'propertyimages', image_filename)
            property_image.save(image_path)
            image_url = f"/static/assets/propertyimages/{image_filename}"
        else:
            image_url = None

        images = image_url

        fraction_price = float(price) / int(fractions)
        available_fractions = fractions

        new_property = Property(name=name, description=description, location=location,  price=price, fractions=fractions, available_fractions=available_fractions,
                            fraction_price=fraction_price, status=status, images=image_url)

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
            session['admin_id'] = admin.id
            session['admin_username'] = admin.username

            # Redirect to the desired page after login (e.g., user's portfolio)
            return redirect(url_for('adminpanel'))
        else:
            # Handle incorrect login credentials (e.g., show an error message)
            return render_template('adminlogin.html', error='Invalid email or password')
    
configure_views(app)
    

if __name__ == '__main__': # ensures the script is executed directly and not when imported as a module
    app.run(host='0.0.0.0', port=8080) #listen on all available network interfaces and on port 8080