from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str = "local"

    API_PREFIX: str = "/api"
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    OAUTH_CLIENT_ID: str
    OAUTH_CLIENT_SECRET: str

    DORY_APP_DEEPLINK: str = "dory://"

    GCLOUD_PROJECT_ID: str = "sandbox-ebaumgartner"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
