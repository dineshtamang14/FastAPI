from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str = "localhost"
    database_name: str
    database_username: str = "postgres"
    secret_key: str = "dfk3kjdfxjek443id64k"
    algorithm: str
    access_token_expire_minutes: int = 45

    class config:
        env_file = ".env"


settings = Settings()
