from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='/app/static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models


@app.before_first_request
def create_tables():
    """Initialize tables"""
    db.create_all()
    from app.models import init_defaults
    init_defaults()
