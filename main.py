from flask import Flask
from flask_restx import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

BRUKERE = {}

class UserList(Resource):
    def post(self):
        parser.add_argument("id")
        parser.add_argument("brukernavn")
        parser.add_argument("epost")
        parser.add_argument("passord")
        args = parser.parse_args()

        # Sjekk at brukernavn og epost er unike
        brukere = list(BRUKERE.values())
        for bruker in brukere:
            if args["brukernavn"] in bruker.values():
                return "Username already in use", 400
            elif args["epost"] in bruker.values():
                return "E-mail already in use", 400

        # Opprett brukar
        BRUKERE[args["id"]] = {
            "id": args["id"],
            "brukernavn": args["brukernavn"],
            "epost": args["epost"],
            "passord": args["passord"],
        }
        print(type(BRUKERE.values()))
        return BRUKERE[args["id"]], 201

    def get(self):
        return BRUKERE


class User(Resource):
    def get(self, id):
        if id not in BRUKERE:
            return "Not Found", 404
        else:
            return BRUKERE[id], 200

    def delete(self, id):
        if id not in BRUKERE:
            return "Not Found", 404
        else:
            del BRUKERE[id]
            return '', 204

api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True)