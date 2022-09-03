from flask_restful import Resource, reqparse
from models.modelo import HotelModel



class Hoteis(Resource):
    def get(self):
        return {'Hoteis':[hotel.json () for hotel in HotelModel.query.all()]} # SELECT * FROM Hoteis

class Hotel(Resource):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be empty")
        atributos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be empty")
        atributos.add_argument('diaria')
        atributos.add_argument('cidade')
    
        def get(self, hotel_id):
            hotel = HotelModel.find_hotel(hotel_id)
            if hotel:
                return hotel.json()   
            return{'message':'Hotel not found.'}, 404

        
        def post(self, hotel_id):
            if HotelModel.find_hotel(hotel_id):
                return{"message":"Hotel id '{}' already exists.".format(hotel_id)}, 400
            dados = Hotel.atributos.parse_args()
            hotel = HotelModel(hotel_id, **dados)
            try:
                hotel.save_hotel()
            except:
                return{'message':'An internal error occurred trying to save the hotel.'}, 500 #Internal server error
            return hotel.json()
            
              
        def put(self, hotel_id):
            dados = Hotel.atributos.parse_args()
            hotel = HotelModel.find_hotel(hotel_id)
            hotel_encontrado = HotelModel.find_hotel(hotel_id)
            if hotel_encontrado:
                hotel_encontrado.update_hotel(**dados)
                hotel_encontrado.save_hotel()
                return hotel_encontrado.json(), 200
            hotel = HotelModel(hotel_id, **dados)
            try:
                hotel.save_hotel()
            except:
                return{'message':'An internal error occurred trying to update the hotel.'}, 500 #Internal server error
            return hotel.json(), 201 # created
            
    
        def delete(self, hotel_id):
            hotel = HotelModel.find_hotel(hotel_id)
            if hotel:
                try:
                    hotel.delete_hotel()
                except:
                        return{'message':'An error occurred trying to delete the hotel'}, 500 # Internal server error
                return{'message':'Hotel deleted.'}
            return{'message':'Hotel not found.'}