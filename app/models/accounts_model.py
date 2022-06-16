from datetime import date, datetime
from app.configs.database import db
from sqlalchemy import Integer, Column, CHAR, VARCHAR, DATE, DATETIME
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

# from app.utils.exceptions import UserNotFoundError, WrongPasswordError
@dataclass
class UserModel(db.Model):
    id: int
    email: str
    first_name: str
    last_name: str
    cpf: str
    phone: str
    birth_date: date
    created_at: datetime

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(255), nullable=False, unique=True)
    password_hash = Column(VARCHAR(255), nullable=False)
    first_name = Column(VARCHAR(150), nullable=False)
    last_name = Column(VARCHAR(150), nullable=False)
    cpf = Column(CHAR(11), nullable=False, unique=True)
    phone = Column(CHAR(11), nullable=True)
    birth_date = Column(DATE(), nullable=True)
    created_at = Column(DATE(), default=datetime.now())

    @property
    def password(self) -> None:
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password=password_to_hash)

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password=password_to_check)

    @classmethod
    def get_id(cls, email: str) -> int:
        fetched_user = cls.query.filter_by(email=email).first()
        return fetched_user.id

    @classmethod
    def fetch_user(cls, email: str, password: str):
        fetched_user = cls.query.filter_by(email=email).first()
        if fetched_user is None:
            raise KeyError
        is_password_correct = fetched_user.check_password(password)
        if is_password_correct:
            return fetched_user
        raise ValueError
