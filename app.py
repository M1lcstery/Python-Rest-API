from flask import Flask
from tasks import tasks_blueprints

app = Flask(__name__)
app.register_blueprint(tasks_blueprints)

if __name__ == '__main__':
    app.run(port=5000)
