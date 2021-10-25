import json

with open('credentials.json') as json_file:
    config = json.load(json_file)

USER = config.get("USER")
PASSWORD = config.get("PASSWORD")
DATABASE = config.get("DATABASE")
JWT_SECRET_KEY = config.get("JWT_SECRET_KEY")
PORT = config.get("PORT")
HOST = config.get("HOST")
DATABASE_URL = config.get("DATABASE_URL")