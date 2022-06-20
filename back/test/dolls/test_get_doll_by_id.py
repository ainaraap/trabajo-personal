from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.dolls import DollsRepository, Doll


def test_should_return_existing__doll_by_id():
    dolls_repository = DollsRepository(temp_file())
    app = create_app(repositories={"dolls": dolls_repository})
    client = app.test_client()

    muneca_1 = Doll(
        doll_id=1,
        user_id="1",
        name="Muñeca sentada",
        price="25.50€",
        img="https://i.ibb.co/HrRB4ty/muneca1.png",
        size="25cm",
    )
    muneca_2 = Doll(
        doll_id=2,
        user_id="1",
        name="Cojín",
        price="29.50€",
        img="https://i.ibb.co/DpKtm2H/muneca2.png",
        size="43cm",
    )

    dolls_repository.save(muneca_1)
    dolls_repository.save(muneca_2)

    response = client.get("/api/dolls/1")

    assert response.status_code == 200
    assert response.json == {
        "doll_id": 1,
        "user_id": "1",
        "name": "Muñeca sentada",
        "price": "25.50€",
        "img": "https://i.ibb.co/HrRB4ty/muneca1.png",
        "size": "25cm",
    }
