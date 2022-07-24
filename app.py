from flask import Flask, render_template , url_for, redirect
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
import requests
load_dotenv()
app = Flask(__name__)
#creating OAuth registry
oauth = OAuth(app)
app.config['SECRET_KEY']= "something unique and secret"
app.config['GITHUB_CLIENT_ID']=os.getenv('GITHUB_CLIENT_ID')
app.config['GITHUB_CLIENT_SECRET']=os.getenv('GITHUB_CLIENT_SECRET')
github = oauth.register (
  name = 'github',
    client_id = app.config["GITHUB_CLIENT_ID"],
    client_secret = app.config["GITHUB_CLIENT_SECRET"],
    access_token_url = 'https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://github.com/login/oauth/authorize',
    authorize_params = None,
    api_base_url = 'https://api.github.com/',
    client_kwargs = {'scope': 'user:email'},
)

@app.route('/')
def Html():
    return render_template('index.html')
    
#Route for Github AOuth
@app.route('/login/github')
def github_login():
    github = oauth.create_client('github')
    redirect_uri = url_for('github_authorize',_external = True) 
    return github.authorize_redirect(redirect_uri)
#Route for Details fetched and return to template
@app.route('/login/github/authorize')
def github_authorize():
    github = oauth.create_client('github')
    token = github.authorize_access_token()
    resp = github.get('user').json()
    user_name = resp["login"]
    avatar_url = resp["avatar_url"]
    return  render_template('user.html',User_name=user_name,User_profile=avatar_url)

if __name__ == '__main__':
    app.run(debug=True)