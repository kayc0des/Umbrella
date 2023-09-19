# import the Flask class from the flask library
from flask import Flask 

# Create an instance of the Flask class
app = Flask(__name__) #__name__ is a special python variable that represents the name of the current module

# Define a route and a view function
@app.route('/') #Defines a route for the root URL - When a user visits the URL Flask calls the hello_world function
def hello_world():
    return 'Hello World!'

if __name__ == '__main__': # ensures the script is executed directly and not when imported as a module
    app.run(host='0.0.0.0', port=8080) #listen on all available network interfaces and onn port 8080