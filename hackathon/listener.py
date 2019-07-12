from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def base():
        return "get base"


#class SubService(Resource):
@app.route('/subService/<subServiceName>', methods=['GET'])
def get(subServiceName):
        return "get"

@app.route('/subService', methods=['POST'])
def create():
        return "create"

@app.route('/subService/<subServiceName>', methods=['DELETE'])
def delete(subServiceName):
        return "delete"

@app.route('/subService/<subServiceName>', methods=['PUT'])
def updated(subServiceName):
        return "update"

#api.add_resource(SubService, '/subService')



if __name__ == '__main__':
     app.run(host='0.0.0.0', port='1501')
