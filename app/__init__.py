from flask import Flask 
from .config import Config
from .db import db,migrate 
from .models import *
from .routes import bakery_bp,baked_good_bp


def create_app():
    app=Flask(__name__)
    
    app.config.from_object(Config)
    app.json.compact=False 

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(bakery_bp,url_prefix="/bakeries")
    app.register_blueprint(baked_good_bp,url_prefix="/baked_goods")

    return app