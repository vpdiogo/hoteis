from sql_alchemy import base

class SiteModel(base.Model):
    __tablename__ = 'sites'

    site_id = base.Column(base.Integer, primary_key=True)
    url = base.Column(base.String(80))
    hoteis = base.relationship('HotelModel') # lista de objetos hoteis

    def __init__(self, url):
        self.url = url

    def json(self):
        return {
            'site_id': self.site_id,
            'url': self.url,
            'hoteis': [hotel.json() for hotel in self.hoteis]

        }

    @classmethod
    def find_site(cls, url):
        site = cls.query.filter_by(url=url).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if site:
            return site
        return None

    @classmethod
    def find_by_id(cls, site_id):
        site = cls.query.filter_by(site_id=site_id).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if site:
            return site
        return None

    def save_site(self):
        base.session.add(self)
        base.session.commit()

    def delete_site(self):
        # deletando todos hoteis associados ao site
        [hotel.delete_hotel() for hotel in self.hoteis]
        # deletando o site
        base.session.delete(self)
        base.session.commit()