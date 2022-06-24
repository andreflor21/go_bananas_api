from app.configs.database import db
from sqlalchemy import Integer, Column, CHAR, VARCHAR, BOOLEAN
from dataclasses import dataclass


@dataclass
class AddressModel(db.Model):
    id: int
    street: str
    number: str
    complement: str
    district: str
    city: str
    state: str
    zip_code: str
    main_address: bool
    user_id: "users_model.UserModel"

    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    street = Column(VARCHAR(250), nullable=False)
    number = Column(VARCHAR(100), nullable=False)
    complement = Column(VARCHAR(250), nullable=True)
    district = Column(VARCHAR(250), nullable=True)
    city = Column(VARCHAR(100), nullable=False)
    state = Column(CHAR(2), nullable=False)
    zip_code = Column(VARCHAR(8), nullable=False)
    main_address = Column(BOOLEAN, default=False)

    user_id = Column(Integer, db.ForeignKey("users.id"), nullable=False)
