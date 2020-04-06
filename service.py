from models import ToDoDB


class ToDoService:
    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        return self.db.create(params['title'], params['description'], params['due_date'])

    def delete(self, params):
        return self.db.create(params['title'], params['description'], params['due_date'])
