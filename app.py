import json
from flask import Flask,request
from predict import predict
app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps({'msg':"Hello World"})

@app.route('/getData',methods=['GET'])
def predict1():
    if request.method == 'GET':
        response = predict('imh')
        print(response['value'][0])
        result = {}
        for i in range(3):
            result[2021 + i] = response['value'][i]
        return json.dumps(result)  
    else:
        return json.dumps({'msg':"Send POST req"})