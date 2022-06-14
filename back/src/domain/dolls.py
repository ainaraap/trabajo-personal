import sqlite3


class Doll:
    def __init__(self, doll_id, user_id, name, price, img, size):
        self.doll_id = doll_id
        self.user_id = user_id
        self.name = name
        self.price = price
        self.img = img
        self.size = size

    def to_dict(self):
        return {
            "doll_id": self.doll_id,
            "user_id": self.user_id,
            "name": self.name,
            "price": self.price,
            "img": self.img,
            "size": self.size,
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
                doll_id integer PRIMARY KEY,
                user_id varchar,
                name text,
                price text,
                img varchar,
                size text
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

    def get_dolls_by_id(self, doll_id):

        sql = """SELECT * FROM dolls WHERE doll_id=:doll_id """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"doll_id": doll_id})

        data = cursor.fetchone()
        doll = Doll(**data)
        return doll

    def save(self, doll):

        sql = """insert into dolls
        (doll_id, user_id, name, price, img, size) values (
            :doll_id, :user_id, :name, :price, :img, :size )"""

        conn = self.create_conn()
        cursor = conn.cursor()

        cursor.execute(sql, doll.to_dict())

        conn.commit()
