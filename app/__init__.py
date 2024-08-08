from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from secure import Secure
secure_headers = Secure()

app = Flask(__name__, static_url_path='/app/static')
app.config.from_object(Config)

bootstrap = Bootstrap5(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models


@app.after_request
def set_secure_headers(response):
    secure_headers.framework.flask(response)
    return response
