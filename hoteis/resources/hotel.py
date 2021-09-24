from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} # SELECT * FROM hoteis

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404 # not found

    def post(self, hotel_id):

        if HotelModel.find_hotel(hotel_id):
            return {'message': f'Hotel id {hotel_id} already exists.'}, 400 # Bad request

        dados = Hotel.argumentos.parse_args()
        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        
        hotel_found = HotelModel.find_hotel(hotel_id)
        if hotel_found:
            hotel_found.update_hotel(**dados)
            hotel_found.save_hotel()
            return hotel_found.json(), 200

        hotel = HotelModel(hotel_id, **dados)
        hotel.save_hotel()        
        return hotel.json(), 201 # created

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted.'}
        
        return {'message': 'Hotel not found.'}, 404