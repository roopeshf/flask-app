from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	user = {'username': 'There'}
	return '''
<html>
    <head>
        <title>Index Page</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <p> This is to test a flask app deployed using jenkins, docker and ansible </p>
    </body>


</html>'''
@app.route('/index')
def index():
    user = {'username': 'There'}
    return '''
<html>
    <head>
        <title>Index Page</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

if __name__ == "__main__":
	app.run(host='0.0.0.0',port='7000')
