from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    title: str = "ReceiptChecker API"
    version: str = "1.0.0"
    environment: str = "dev"

    class Config:
        env_prefix = "APP_"


class GASConfig(BaseSettings):
    get_calendar_url: str

    class Config:
        env_prefix = "GAS_"


class Settings:
    app: AppConfig = AppConfig()
    gas: GASConfig = GASConfig()
