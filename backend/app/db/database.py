from collections.abc import Generator

from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel, create_engine

from app.config import settings

# Registra los metadatos de SQLModel antes de ejecutar create_all.
import app.models  # noqa: F401


engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)


def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session


def create_db_and_tables() -> None:
    """Crea las tablas una vez registrados los modelos de SQLModel."""
    if not SQLModel.metadata.tables:
        return

    SQLModel.metadata.create_all(engine)
