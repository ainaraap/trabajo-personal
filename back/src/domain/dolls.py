import sqlite3


class Doll:
    def __init__(self, doll_id, size, price, photo):
        self.doll_id = doll_id
        self.size = size
        self.price = price
        self.photo = photo

    def to_dict(self):
        return {
            "doll_id": self.doll_id,
            "size": self.size,
            "price": self.price,
            "photo": self.photo,
        }


class DollsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists dolls (
                doll_id integer,
                size text,
                price integer,
                photo text
                )
                """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    
    def get_dolls(self):
        sql = """select * from dolls"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        result = []
        for item in data:
            doll = Doll(**item)
            result.append(doll)

        return result

    def save(self, doll):

        sql = """insert into dolls
        (doll_id, size, price, photo) values (
            :doll_id, :size, :price, :photo )"""

        conn = self.create_conn()
        cursor = conn.cursor()

        cursor.execute(sql, doll.to_dict())

        conn.commit()
