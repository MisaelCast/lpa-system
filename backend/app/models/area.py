from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.models.usuario_area import UsuarioArea

if TYPE_CHECKING:
    from app.models.auditoria import Auditoria
    from app.models.celula import Celula
    from app.models.usuario import Usuario


class Area(SQLModel, table=True):
    """Area de produccion donde se realizan auditorias."""

    __tablename__ = "area"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150, unique=True, index=True)
    descripcion: str | None = Field(default=None, max_length=255)
    activa: bool = Field(default=True)

    celulas: list["Celula"] = Relationship(back_populates="area")
    auditorias: list["Auditoria"] = Relationship(back_populates="area")
    usuarios: list["Usuario"] = Relationship(
        back_populates="areas",
        link_model=UsuarioArea,
    )
