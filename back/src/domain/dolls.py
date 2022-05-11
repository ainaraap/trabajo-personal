import sqlite3


class Doll:
    def __init__(self, doll_id, size, price, img):
        self.doll_id = doll_id
        self.size = size
        self.price = price
        self.img = img

    def to_dict(self):
        return {
            "doll_id": self.doll_id,
            "size": self.size,
            "price": self.price,
            "img": self.img,
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
                img varchar
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

    def get_by_id(self, doll_id):

        sql = """SELECT * FROM dolls WHERE id= :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": doll_id})

        data = cursor.fetchone()
        one_doll = Doll(doll_id=data["doll_id"], size=data["size"], price=data["price"], img=data["img"])
        return one_doll


    def save(self, doll):

        sql = """insert into dolls
        (doll_id, size, price, img) values (
            :doll_id, :size, :price, :img )"""

        conn = self.create_conn()
        cursor = conn.cursor()

        cursor.execute(sql, doll.to_dict())

        conn.commit()
