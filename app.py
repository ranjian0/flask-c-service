from flask import Flask 
from services import SumService

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/services/sum/<id>')
def service_sum(id):
    service = SumService()
    result = service.sum(list(range(int(id))))
    return f"Sum for the first {id} numbers is {int(result)}"