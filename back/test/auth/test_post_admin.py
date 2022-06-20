from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UserRepository, User


def setup():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"user": user_repository})
    client = app.test_client()

    ana = User(id="user-1", name="Ana", password="ainaramaider")
    user_repository.save(ana)

    return client


def test_should_validate_admin():
    client = setup()

    body = {"user": "user-1", "password": "ainaramaider"}
    response = client.post("/auth/admin", json=body)

    assert response.status_code == 200
    assert response.json == {"id": "user-1", "name": "Ana"}


def test_should_fail_if_invalid_password():
    client = setup()

    body = {"user": "user-1", "password": "maiderainara"}
    response = client.post("/auth/admin", json=body)

    assert response.status_code == 401


def test_should_fail_if_user_not_exists():
    client = setup()

    body = {"user": "user-not-exists", "password": "arepalo"}
    response = client.post("/auth/admin", json=body)

    assert response.status_code == 401
