#!flask/bin/python

from flask import Flask, jsonify, request, render_template
import  sys
import json
from bson import json_util
from  twCollector.mongoutils import MongodbReader


app = Flask(__name__, template_folder='template')
PATH=sys.path[0]
item=None;
client = MongodbReader();


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')


@app.route('/list', methods=['GET'])
def list():
    global item
    item=client.getOneItem()
    return  json.dumps(item,default=json_util.default);

@app.route('/previous', methods=['GET'])
def previousTweet():
    global item
    item=client.getPreviousItem()
    return  json.dumps(item,default=json_util.default);

@app.route('/save', methods=['POST'])
def save():
    global item
    data = request.json
    for i in range(0,len(data)):

        item["wordsoftweets"][data[i]["Words"]]=data[i]["Label"]

    result=client.updateOneItem(item["_id"],item["wordsoftweets"])
    if result['updatedExisting']==True:
        return json.dumps({"status":0})
    else:
        return json.dumps({"status": 1})


if __name__ == '__main__':
    app.run(port=3250)
