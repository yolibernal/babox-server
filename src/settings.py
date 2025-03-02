from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gpio_enabled: bool = False

    port: int = 5001
    host: str = "0.0.0.0"


settings = Settings()
