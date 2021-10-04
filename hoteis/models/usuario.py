from sql_alchemy import base

class UserModel(base.Model):
    __tablename__ = 'usuarios'

    user_id = base.Column(base.Integer, primary_key=True)
    login = base.Column(base.String(40))
    senha = base.Column(base.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first() # SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if user:
            return user
        return None

    def save_user(self):
        base.session.add(self)
        base.session.commit()

    def delete_user(self):
        base.session.delete(self)
        base.session.commit()