from flask_restful import Resource, reqparse
from models.modelo import HotelModel


hoteis =[
    {
        'hotel_id':'jamaica',
        'nome':'Jamaica Hotel',
        'estrelas':4.3,
        'diaria': 420.42,
        'cidade':'Kingston'
    },
     {
        'hotel_id':'amsterdam',
        'nome':'Amsterdam Hotel',
        'estrelas':4.9,
        'diaria': 450.35,
        'cidade':'Amsterdam'
    },
     {
        'hotel_id':'montevideo',
        'nome':'Montevideo Hotel',
        'estrelas':4.2,
        'diaria': 342.00,
        'cidade': 'Montevideo'
    }
    
]
class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
       self.hotel_id = hotel_id
       self.nome = nome
       self.estrelas = estrelas
       self.diaria = diaria
       self.cidade = cidade 

    def json(self):
        return{
            'hotel_id' : self.hotel_id,
            'nome': self.nome,
            'estrela': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

class Hoteis(Resource):
    def get(self):
        return {'Hoteis':hoteis}

class Hotel(Resource):
        atributos = reqparse.RequestParser()
        atributos.add_argument('nome')
        atributos.add_argument('estrelas')
        atributos.add_argument('diaria')
        atributos.add_argument('cidade')
        
        def find_hotel(hotel_id):
            for hotel in hoteis:
                if hotel['hotel_id'] == hotel_id:
                    return hotel
            return None
    
        def get(self, hotel_id):
            hotel = Hotel.find_hotel(hotel_id)
            if hotel:
                return hotel
            return{'message':'Hotel not found.'}, 404

        
        def post(self, hotel_id):
            dados = Hotel.atributos.parse_args()
            hotel_objeto = HotelModel(hotel_id, **dados)
            novo_hotel= hotel_objeto.json()
            hoteis.append(novo_hotel)
            return novo_hotel, 201
        

        
        def put(self, hotel_id):
            dados = Hotel.atributos.parse_args()
            hotel_objeto = HotelModel(hotel_id, **dados)
            novo_hotel= hotel_objeto.json()
            hotel = Hotel.find_hotel(hotel_id)
            if hotel:
                hotel.update(novo_hotel)
            return novo_hotel, 201 # update
            
    
        def delete(self, hotel_id):
            global hoteis
            hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
            return{'message':'Hotel deleted.'}