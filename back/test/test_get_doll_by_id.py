from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.dolls import DollsRepository, Doll


def test_shuld_return_doll_by_id():
    dolls_repository = DollsRepository(temp_file())
    app = create_app(repositories={"dolls": dolls_repository})
    client = app.test_client()

    muneca_1 = Doll(
        doll_id=1,
        name="Muñeca sentada",
        price="25.50 €",
        img="https://i.ibb.co/HrRB4ty/muneca1.png",
    )
    dolls_repository.save(muneca_1)

    response = client.get("/api/dolls/1")

    assert response.status_code == 200
    assert response.json == [
        {
            "doll_id": 1,
            "name": "Muñeca sentada",
            "price": "25.50 €",
            "img": "https://i.ibb.co/HrRB4ty/muneca1.png",
        }
    ]
