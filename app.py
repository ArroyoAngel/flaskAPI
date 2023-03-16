from flask import Flask
from flask_cors import CORS
from src.app.activity.application.controllers import activity_controller
from flask_cors import cross_origin
from flask_bcrypt import Bcrypt

if __name__ == "__main__":""

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def cors_headers():
    return 'CORS ENABLED'

app.register_blueprint(activity_controller)

CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flaskapi'
bcrypt = Bcrypt(app)
app.run(debug=True, host="0.0.0.0")