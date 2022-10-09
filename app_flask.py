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

    return answer(items=res, count=len(res))

@app.route('/insert', methods=['POST'])
def insert():
    collection, data = prepare_param(request)
    if not (type(data) is list):
        data = [data]

    records = collection.insert_many(data)
    id_list = list(map(str, records.inserted_ids))
    
    return answer(inserted_ids=id_list, count=len(id_list))

@app.route('/delete', methods=['POST'])
def delete():
    collection, query = prepare_param(request)
    ans = collection.delete_many(query)
    
    return answer(count=ans.deleted_count)

def prepare_param(request):
    collect = request.args.get('collect')
    collection = mongo.db[collect]

    query_json = request.data.decode()
    query = json.loads(query_json)

    return (collection, query)

def answer(**kwarg):
    ans = {'result': 'ok'}
    for k,v in kwarg.items():
        ans[k] = v

    return json.dumps(ans, indent=2)

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)
