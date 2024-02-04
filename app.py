
# Importing flask module is mandatory
from flask import Flask

# '__name__' is special built in variable, when py runs script directly '__name__' become '__main__'
app = Flask(__name__)
# creates instance of flask class, representing web application

# The route() function of the Flask class is a decorator, 

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	print('heoola')
	return 'Hello World'

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run(host="0.0.0.0",port=5000)

