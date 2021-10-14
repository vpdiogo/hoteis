from sql_alchemy import base

class HotelModel(base.Model):
    __tablename__ = 'hoteis'

    hotel_id = base.Column(base.String, primary_key=True)
    nome = base.Column(base.String(80))
    estrelas = base.Column(base.Float(precision=1))
    diaria = base.Column(base.Float(precision=2))
    cidade = base.Column(base.String(40))
    site_id = base.Column(base.Integer, base.ForeignKey('sites.site_id'))
    # site = base.relationship('SiteModel')

    def __init__(self, hotel_id, nome, estrelas, diaria, cidade, site_id):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
        self.site_id = site_id

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade,
            'site_id': self.site_id

        }

    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        base.session.add(self)
        base.session.commit()

    def update_hotel(self, nome, estrelas, diaria, cidade):
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def delete_hotel(self):
        base.session.delete(self)
        base.session.commit()