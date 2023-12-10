from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from .config import config


engine = create_engine(
    f"postgresql+psycopg2://{config.pg.user}:{config.pg.password}@{config.pg.host}:5432/{config.pg.db}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
