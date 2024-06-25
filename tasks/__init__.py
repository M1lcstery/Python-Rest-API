from flask import Blueprint, jsonify, request

tasks_blueprints = Blueprint("tasks", __name__)

# Get all tasks
@tasks_blueprints.route("/tasks", methods=["GET"])
def get_tasks():
    ""
    
# Get task by ID
@tasks_blueprints.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    ""
    
# Create a task
@tasks_blueprints.route("/tasks", methods=["POST"])
def create_task():
    ""
    
# Delete a task
@tasks_blueprints.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    ""
    
# Update a task
@tasks_blueprints.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    ""