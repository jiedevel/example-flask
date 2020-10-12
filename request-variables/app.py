from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#http://localhost:5000/welcome/user
@app.route('/welcome/<username>')
def welcome_user(username):
    return 'Welcome %s' %username

#http://localhost:5000/welcome/user
@app.route('/hello/<string:username>')
def welcome_user_string(username):
    return 'Welcome %s' %username
 
#http://localhost:5000/hi?username=user
@app.route('/hi')
def welcome_user_arg():
     username= request.args.get('username')
     return 'Welcome %s' %username

@app.route('/profile', methods=['POST'])
def welcome_user_json():
     username= request.json['username']
     return 'Welcome %s' %username 

if __name__=='__main__':
    app.run(debug=True)
