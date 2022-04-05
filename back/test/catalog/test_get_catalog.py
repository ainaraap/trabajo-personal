from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.dolls import DollsRepository, Doll


def test_should_return_catalog():
    dolls_repository = DollsRepository(temp_file())
    app = create_app(repositories={"dolls": dolls_repository})
    client = app.test_client()

    muneca_1 = Doll(
        doll_id=1, 
        size="25 cm", 
        price=25.50, 
        photo="URL1"
    )

    muneca_2 = Doll(
        doll_id=2, 
        size="30 cm", 
        price=29.50, 
        photo="URL2"
    )

    dolls_repository.save(muneca_1)
    dolls_repository.save(muneca_2)

    response = client.get("/api/dolls")
    response.status_code == 200
    assert response.json == [
        {
            "doll_id": 1,
            "size": "25 cm",
            "price": 25.50,
            "photo": "URL1",
        },
        {
            "doll_id": 2,
            "size": "30 cm",
            "price": 29.50,
            "photo": "URL2",
        },
    ]
