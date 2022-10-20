import uvicorn
from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles

app = FastAPI()
# app.mount("/files", StaticFiles(directory="/home/nadulich/py/"), name="static")

@app.get("/")
def read_root():
    return {"Text": "Hello, I'm FastAPI"}

@app.get("/ping")
def read_root():
    return {"pong":"ok"}


# @app.route('/find', methods=['GET','POST'])
# def find():

    # collection, query = prepare_param(request, 'find')

    # items = collection.find(query)
    
    # res = []
    # for item in items:
    #     item['_id'] = str(item['_id'])
    #     res.append(item)

    # return answer(items=res, count=len(res))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)