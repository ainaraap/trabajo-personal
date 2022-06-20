import sqlite3

from src.domain.dolls import DollsRepository
from src.domain.user import UserRepository
from src.webserver import create_app


database_path = "data/dolls.db"

repositories = {
    "dolls": DollsRepository(database_path),
    "user": UserRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
