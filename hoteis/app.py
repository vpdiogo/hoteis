from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_base():
    base.create_all()

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import base
    base.init_app(app)
    app.run(debug=True)