import sys


sys.path.insert(0, "")

from src.domain.dolls import Doll, DollsRepository
from src.domain.user import UserRepository, User


database_path = "data/dolls.db"

user_repository = UserRepository(database_path)
user_repository.save(User(id="user-1", name="Ana", password="ainaramaider"))


muneca_1 = Doll(
    doll_id=1,
    user_id="user-1",
    name="Muñeca sentada",
    price="25.50€",
    img="https://i.ibb.co/jGf5KPS/muneca1.png",
    size="25cm",
)
muneca_2 = Doll(
    doll_id=2,
    user_id="user-1",
    name="Cojín",
    price="29.50€",
    img="https://i.ibb.co/4PK90b5/muneca2.png",
    size="43cm",
)
muneca_3 = Doll(
    doll_id=3,
    user_id="user-1",
    name="Muñeca portapapel WC ",
    price="30€",
    img="https://i.ibb.co/M1SKQ7t/muneca3.png",
    size="55cm",
)
muneca_4 = Doll(
    doll_id=4,
    user_id="user-1",
    name="Muñeca llavero ",
    price="15€",
    img="https://i.ibb.co/z66d2D3/muneca4.png",
    size="15cm",
)
muneca_5 = Doll(
    doll_id=5,
    user_id="user-1",
    name="Muñeca bailarina",
    price="30€",
    img="https://i.ibb.co/cwJ2QYH/muneca5.png",
    size="40cm",
)
muneca_6 = Doll(
    doll_id=6,
    user_id="user-1",
    name="Muñeca Pepona",
    price="20€",
    img="https://i.ibb.co/JjxJt2B/muneca6.png",
    size="20cm",
)
muneca_7 = Doll(
    doll_id=7,
    user_id="user-1",
    name="Muñeco Pepón",
    price="10.50€",
    img="https://i.ibb.co/p1h1PXp/muneca7.png",
    size="10cm",
)


dolls_repository = DollsRepository(database_path)
dolls_repository.save(muneca_1)
dolls_repository.save(muneca_2)
dolls_repository.save(muneca_3)
dolls_repository.save(muneca_4)
dolls_repository.save(muneca_5)
dolls_repository.save(muneca_6)
dolls_repository.save(muneca_7)

print("Base de datos creada")
