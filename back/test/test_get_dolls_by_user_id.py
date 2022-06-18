from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.dolls import DollsRepository, Doll


def test_should_return_list_of_dolls_by_user_id():

    dolls_repository = DollsRepository(temp_file())
    app = create_app(repositories={"dolls": dolls_repository})
    client = app.test_client()

    muneca_1 = Doll(
        doll_id=1,
        user_id="user-Ana",
        name="Muñeca sentada",
        price="25.50€",
        img="https://i.ibb.co/jGf5KPS/muneca1.png",
        size="25cm",
    )
    muneca_2 = Doll(
        doll_id=2,
        user_id="user-Mai",
        name="Cojín",
        price="29.50€",
        img="https://i.ibb.co/4PK90b5/muneca2.png",
        size="43cm",
    )

    dolls_repository.save(muneca_1)
    dolls_repository.save(muneca_2)

    response = client.get("/api/dolls", headers={"Authorization": "user-Ana"})

    response.json == {
        "doll_id": 1,
        "user_id": "1",
        "name": "Muñeca sentada",
        "price": "25.50€",
        "img": "https://i.ibb.co/HrRB4ty/muneca1.png",
        "size": "25cm",
    }
