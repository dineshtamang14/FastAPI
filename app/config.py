from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str
    database_name: str = "postgres"
    database_username: str = "postgres"
    secret_key: str = "dkjgi83jfkdjdt343df"
    algorithm: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"


settings = Settings()