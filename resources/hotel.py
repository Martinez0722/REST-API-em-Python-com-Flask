from flask_restful import Resource, reqparse
from models.modelo import HotelModel


# hoteis =[
#     {
#         'hotel_id':'jamaica',
#         'nome':'Jamaica Hotel',
#         'estrelas':4.3,
#         'diaria': 420.42,
#         'cidade':'Kingston'
#     },
#      {
#         'hotel_id':'amsterdam',
#         'nome':'Amsterdam Hotel',
#         'estrelas':4.9,
#         'diaria': 450.35,
#         'cidade':'Amsterdam'
#     },
#      {
#         'hotel_id':'montevideo',
#         'nome':'Montevideo Hotel',
#         'estrelas':4.2,
#         'diaria': 342.00,
#         'cidade': 'Montevideo'
#     }
    
# ]

class Hoteis(Resource):
    def get(self):
        return {'Hoteis':[hotel.json () for hotel in HotelModel.query.all()]} # SELECT * FROM Hoteis

class Hotel(Resource):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome')
        atributos.add_argument('estrelas')
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
            hotel.save_hotel()
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
            hotel.save_hotel()
            return hotel.json(), 201 # created
            
    
        def delete(self, hotel_id):
            hotel = HotelModel.find_hotel(hotel_id)
            if hotel:
                hotel.delete_hotel()
                return{'message':'Hotel deleted.'}
            return{'message':'Hotel not found.'}