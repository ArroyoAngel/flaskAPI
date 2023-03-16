from flask import Flask
from flask_cors import CORS
from src.app.activity.application.controllers import activity_controller
from flask_cors import cross_origin

if __name__ == "__main__":""

DB_NAME = "flaskapi"
USER_DB = "luis"
USER_PWD = "luis123"
URL = f"mongodb://{USER_DB}:{USER_PWD}@localhost:27017"

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def cors_headers():
    return 'CORS ENABLED'

app.register_blueprint(activity_controller)

CORS(app)
app.config['MONGO_URI'] = f'{URL}/{DB_NAME} --auth'
app.run(debug=True, host="0.0.0.0")