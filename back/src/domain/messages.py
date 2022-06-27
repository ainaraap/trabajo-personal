import sqlite3


class Message:
    def __init__(self, name, phone, message):
        self.name = name
        self.phone = phone
        self.message = message

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "message": self.message,
        }


class MessagesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists messages (
                name text,
                phone text,
                message text
                )
                """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_messages(self):
        sql = """select * from messages"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            message = Message(**item)
            result.append(message)

        return result

    def save(self, message):

        sql = """insert into messages
        (name, phone, message) values (
            :name, :phone, :message )"""

        conn = self.create_conn()
        cursor = conn.cursor()

        cursor.execute(sql, message.to_dict())

        conn.commit()
