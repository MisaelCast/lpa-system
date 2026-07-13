from sqlalchemy.engine import URL
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "LPA System API"
    app_description: str = "Backend API for LPA System."
    app_version: str = "0.1.0"
    environment: str = "development"

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "lpa_system"
    database_user: str = "postgres"
    database_password: str = "postgres"

    backend_cors_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    @property
    def database_url(self) -> str:
        """Build the PostgreSQL connection URL from environment settings."""
        url = URL.create(
            drivername="postgresql+psycopg",
            username=self.database_user,
            password=self.database_password,
            host=self.database_host,
            port=self.database_port,
            database=self.database_name,
        )
        return url.render_as_string(hide_password=False)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
