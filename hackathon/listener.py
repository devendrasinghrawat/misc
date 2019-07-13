from flask import Flask, request
from flask_restful import Resource, Api
import json
import subprocess

app = Flask(__name__)
#api = Api(app)
basePath = '/var/edge/'
data = [];

@app.route('/')
def base():
        return "get base"


#class SubService(Resource):
@app.route('/subservice/<subServiceName>', methods=['GET'])
def get(subServiceName):
        return "get"

@app.route('/subservice/<subServiceName>', methods=['POST'])
def create(subServiceName):
        with open('policy.json') as policy_file:
                policy=json.load(policy_file)
                for subService in policy['services']:
                        if subServiceName == subService['name']:
                                print("After if")
                                data.append(subService['name'])
                                data.append(subService['image_src'])
                                data.append(subService['docker-compose_config'])
                                data.append(subService['docker-compose_start_params'])

                                servicedir = basePath + data[0]
                                cmd = 'mkdir ' + servicedir
                                subprocess.call(cmd,shell=True)
                                print(servicedir)
                                cmd = 'wget ' + data[2]
                                subprocess.call(cmd,shell=True)
                                cmd = 'mv ' + basePath+ 'docker-compose.yml ' + servicedir
                                subprocess.call(cmd,shell=True)
                                cmd = 'docker pull ' + data[1]
                                subprocess.call(cmd,shell=True)
                                cmd = 'docker-compose -f '+ servicedir + '/docker-compose.yml up -d'
                                subprocess.call(cmd,shell=True)

                print(data)

                return data[2]

@app.route('/subservice/<subServiceName>', methods=['DELETE'])
def delete(subServiceName):
        return "delete"

@app.route('/subservice/<subServiceName>', methods=['PUT'])
def updated(subServiceName):
        return "update"

#api.add_resource(SubService, '/subService')

def read_file() :
        return "read"


if __name__ == '__main__':
     app.run(host='0.0.0.0', port='1501')
