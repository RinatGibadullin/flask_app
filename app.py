from flask import Flask
from flask import request
from service import ToDoService

app = Flask(__name__)


@app.route('/todo', methods=["POST"])
def create_todo():
    result = ToDoService().create(request.get_json())
    return result.to_json()


@app.route('/todo', methods=["DELETE"])
def delete_todo():
    result = ToDoService().create(request.get_json())
    return result.to_json()


if __name__ == '__main__':
    app.run(debug="true")
