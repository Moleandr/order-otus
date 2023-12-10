from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

from src.database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    items: Mapped[list[str]] = mapped_column(ARRAY(String))


class Operation(Base):
    __tablename__ = "operations"
    id: Mapped[str] = mapped_column(primary_key=True, unique=True)
