'''
Rfr this link for the proj explanation
https://medium.com/@pravallikaperavali99/ep03-docker-container-project-510e08edd99a

Step 2: Creating a Flask Python App
The Flask application serves as a simple login page (‘login.html’) and welcomes 
users with a personalized message based on the provided name. 
It handles both form submissions and URL parameters for flexibility in user input. 
The application is set up to run on port 3000, accessible externally, 
with the development server listening on all network interfaces.
'''

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'Welcome, {}'.format(name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)