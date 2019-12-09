from flask import request, jsonify

from api.index import home_blu
from api.index.utils.handle_json import handle_json


@home_blu.route('/home')
def home():
  path = request.args.get('path')
  json_dict = handle_json(path)
  return jsonify(json_dict)


# @home_blu.route('/home')
# def home():
#   response_dict = {
#     'data': {'city': '北京'},
#     'ret': True
#   }
#   response = jsonify(response_dict)
#   return response, 200
