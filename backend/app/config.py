from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "LPA System API"
    app_description: str = "Backend API for LPA System."
    app_version: str = "0.1.0"
    environment: str = "development"

    database_url: str = "postgresql://postgres:postgres@localhost:5432/lpa_system"
    backend_cors_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
