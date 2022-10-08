from flask import Flask, request, json
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://gitsrv01:27017/nadulich"
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_info():
    return '{"info":"GET"}'

@app.route('/ping', methods=['GET'])
def pong():
    return '{"pong":"ok"}'

@app.route('/find', methods=['GET','POST'])
def find():

    collection, query = prepare_param(request)

    items = collection.find(query)
    
    res = []
    for item in items:
        item['_id'] = str(item['_id'])
        res.append(item)

    return json.dumps(res, indent=4)

@app.route('/insert_one', methods=['POST'])
def insert_one():
    collection, query = prepare_param(request)

    items = collection.insert_one(query)

    return "{'result':'ok'}"

def prepare_param(request):
    collect = request.args.get('collect')
    collection = mongo.db[collect]

    query_json = request.data.decode()
    query = json.loads(query_json)

    return (collection, query)


if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
