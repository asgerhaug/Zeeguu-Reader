from flask import Flask, render_template, request, make_response
import requests

ZEEGUU_SERVER = "https://www.zeeguu.unibe.ch"
STATUS_WRONGUSER  = 401; STATUS_WRONGPASS = 400; STATUS_ACCEPT = 200;

app = Flask(__name__)

# Main entrypoint, asks the user to login before continuing.       
@app.route('/', methods=['GET', 'POST'])
def entrypage():
    if 'sessionID' in request.cookies:
        return home(request.cookies.get('sessionID'))
    else:
        if request.method == 'POST':
            return login_handle()
        else:
            return login_form()

# Ask the user to fill in login credentials.
def login_form():
    return render_template('login.html')

# Handle login request.
def login_handle():
    username = request.form['username']
    password = {'password' : request.form['password']}
    result = requests.post(ZEEGUU_SERVER+'/session/'+username, password)
    
    # Check for login succces, sends the user back to login or continues.
    if (result.status_code == STATUS_WRONGUSER or result.status_code == STATUS_WRONGPASS):
        response = make_response(login_form())
    else:
        sessionID = result.content
        response = make_response(home(sessionID))
        response.set_cookie('sessionID', sessionID)
    return response;

# Display the home page.
def home(sessionID):
    print sessionID
    return render_template('article.html')
