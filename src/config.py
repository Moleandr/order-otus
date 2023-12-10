from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Postgres(BaseModel):
    host: str
    user: str = 'app'
    password: str
    db: str = 'app'


class Config(BaseSettings):
    pg: Postgres
    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        env_file='.env'
    )


config = Config()
