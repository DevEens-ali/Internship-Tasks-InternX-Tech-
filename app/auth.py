import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
SECRET_KEY = "my_super_secret_key"
ALGORITHM = "HS256"

def hash_password(password: str):
    hashed_password = bcrypt.hashpw(
        password.encode("UTF-8"),
        bcrypt.gensalt()
    )

    return hashed_password.decode("UTF-8")


def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    payload["exp"] = expire

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token