from flask import Flask
from flask_cors import CORS
from src.app.activity.application.controllers import activity_controller
from src.app.auth.application.controllers import auth_controller
from src.app.user.application.controllers import user_controller
from src.app.pond.application.controllers import pond_controller
from src.app.product.application.controllers import product_controller
from flask_cors import cross_origin

if __name__ == "__main__":""

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flaskapi'

@app.route('/', methods=['GET'])
@cross_origin()
def cors_headers():
    return 'CORS ENABLED'

app.register_blueprint(activity_controller)
app.register_blueprint(auth_controller)
app.register_blueprint(user_controller)
app.register_blueprint(pond_controller)
app.register_blueprint(product_controller)

CORS(app)
app.run(debug=True, host="0.0.0.0")