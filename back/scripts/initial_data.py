import sys

sys.path.insert(0, "")

from src.domain.dolls import Doll, DollsRepository

database_path = "data/dolls.db"

doll_repository = DollsRepository(database_path)


muneca_1 = Doll(
        doll_id= 1,
        size= "25 cm",
        price= 25.50,
        photo= "URL1"
)
muneca_2 = Doll(
        doll_id=  2,
        size= "30 cm",
        price= 29.50,
        photo= "URL2"
)

dolls_repository = DollsRepository(database_path)
dolls_repository.save(muneca_1)
dolls_repository.save(muneca_2)





