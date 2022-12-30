from bson.json_util import _json_convert

from app.db import app
from app.auth.routes import accounts
from app.users.routes import users

app.register_blueprint(users)
#print(app.url_map)

if __name__ == "__main__":""
app.run(debug=True)