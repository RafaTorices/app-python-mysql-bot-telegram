from application.config import MySQLConfig


class MySQL():
    def __init__(self):
        config = MySQLConfig()
        self.host = config.DB_HOST
        self.user = config.DB_USER
        self.password = config.DB_PASSWORD
        self.db = config.DB_NAME
        self.port = config.DB_PORT
