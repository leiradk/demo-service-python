"""This is a assignment for the interview."""
# importing dependencies or modules
from flask import Flask
from flask_restful import Api
from resources.processStatistics import Statistics

app = Flask(__name__)
api = Api(app)

# adding resource and set route /
api.add_resource(Statistics, '/')

# Run the main app
if __name__ == '__main__':
    app.run(debug=True, port=5000)