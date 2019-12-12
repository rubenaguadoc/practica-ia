from aEstrella import algoritmo as aStar
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask("tokyio")
CORS(app)
api = Api(app)

class Stations(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument("inicio")
    parser.add_argument("fin")
    parser.add_argument("transbordos")
    args = parser.parse_args()

    result, lines = aStar(int(args["inicio"]), int(args["fin"]), args["transbordos"] == "True")
    return {
      "result": result,
      "lines": lines 
    }

api.add_resource(Stations, "/")

app.run(debug=True, port=4567)