import sys

sys.path.insert(0, "")

from src.domain.dolls import Doll, DollsRepository

database_path = "data/dolls.db"

doll_repository = DollsRepository(database_path)


muneca_1 = Doll(
        doll_id= 1,
        name= "Muñeca sentada",
        price= "25.50 €",
        img= "https://i.ibb.co/HrRB4ty/muneca1.png"
)
muneca_2 = Doll(
        doll_id=  2,
        name= "Cojín",
        price= "29.50 €",
        img= "https://i.ibb.co/DpKtm2H/muneca2.png"
)
muneca_3 = Doll(
        doll_id=  3,
        name= "Muñeca portapapel WC ",
        price= "30 €",
        img= "https://i.ibb.co/n6hG04G/muneca3.jpg"
)

dolls_repository = DollsRepository(database_path)
dolls_repository.save(muneca_1)
dolls_repository.save(muneca_2)
dolls_repository.save(muneca_3)

print("Base de datos creada")



