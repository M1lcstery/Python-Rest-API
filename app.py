from flask import Flask
from models import db
from dotenv import load_dotenv
from task_blueprint import task_blueprint
from user_blueprint import user_blueprint
import os

if __name__ == "__main__":
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.register_blueprint(task_blueprint)
    app.register_blueprint(user_blueprint)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)