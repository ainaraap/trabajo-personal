import sys

sys.path.insert(0, "")

from src.domain.dolls import Doll, DollsRepository

database_path = "data/dolls.db"

doll_repository = DollsRepository(database_path)


muneca_1 = Doll(
    doll_id=1,
    name="Muñeca sentada",
    price="25.50€",
    img="https://i.ibb.co/jGf5KPS/muneca1.png",
    size="25cm",
)
muneca_2 = Doll(
    doll_id=2,
    name="Cojín",
    price="29.50€",
    img="https://i.ibb.co/4PK90b5/muneca2.png",
    size="43cm",
)
muneca_3 = Doll(
    doll_id=3,
    name="Muñeca portapapel WC ",
    price="30€",
    img="https://i.ibb.co/FYSpNL3/muneca3.png",
    size="55cm",
)
muneca_4 = Doll(
    doll_id=4,
    name="Muñeca llavero ",
    price="15€",
    img="https://i.ibb.co/z66d2D3/muneca4.png",
    size="15cm",
)

dolls_repository = DollsRepository(database_path)
dolls_repository.save(muneca_1)
dolls_repository.save(muneca_2)
dolls_repository.save(muneca_3)
dolls_repository.save(muneca_4)

print("Base de datos creada")
