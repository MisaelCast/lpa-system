from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.usuario import Usuario


class Rol(SQLModel, table=True):
    """Rol de acceso asignado a un usuario."""

    __tablename__ = "rol"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, unique=True, index=True)
    descripcion: str | None = Field(default=None, max_length=255)

    usuarios: list["Usuario"] = Relationship(back_populates="rol")
