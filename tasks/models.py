from . import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):  # Helper function to serialize the task object
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
