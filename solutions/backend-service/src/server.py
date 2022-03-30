import os
import flask
import json
from db_manager import DBManager

server = flask.Flask(__name__)
db_manager = None

@server.route('/put-item/<item>', methods=['PUT'])
def put(item):
    db_manager.put_item_into_db(item)
    return "Successful"

@server.route('/list', methods=['GET'])
def list():
    response = db_manager.get_items()
    items_list = [p['todo'] for p in response['Items']]
    return "<br/>".join(items_list)


if __name__ == '__main__':
    endpoint = os.getenv('ENDPOINT')
    db_manager = DBManager(database_table='ToDoList', pk_attribute_name='date_time', sk_attribute_name='todo', endpoint=endpoint)
    server.run(debug=True, host='0.0.0.0', port=5000)
