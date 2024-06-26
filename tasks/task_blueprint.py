from flask import Blueprint, jsonify, request, abort
from models import Task, db
from datetime import datetime

task_blueprint = Blueprint('task_blueprint', __name__)

# Gets and returns all tasks
@task_blueprint.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Gets and returns a task with a specific ID
@task_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

# Gets and returns the tasks of a specific user
@task_blueprint.route('/tasks/user/<int:user_id>', methods=['GET'])
def get_tasks_by_user(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    tasks = [task.to_dict() for task in tasks]
    return jsonify(tasks)

# Creates a task
@task_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    due_date = datetime.strptime(data['due_date'], '%d-%m-%Y')
    task = Task(title=data['title'], description=data['description'], due_date=due_date,
                done=data['done'], user_id=data['user_id'])

    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict())

# Update a task
@task_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)

    request_title = request.json.get('title')
    request_description = request.json.get('description')
    request_due_date = datetime.strptime(request.json.get('due_date'), '%d-%m-%Y')
    request_done = request.json.get('done')

    if all((task.title, task.description, task.due_date)) and task.done is not None:
        task.title = request_title
        task.description = request_description
        task.due_date = request_due_date
        task.done = request_done

        db.session.commit()
        return jsonify(task.to_dict())
    else:
        return abort(400, {'error': "Couldn't update task."})

# Delete a task
@task_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()
    return jsonify({})