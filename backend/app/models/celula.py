from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.area import Area
    from app.models.ejecucion_auditoria import EjecucionAuditoria


class Celula(SQLModel, table=True):
    """Linea o celula de produccion dentro de un area."""

    __tablename__ = "celula"

    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150, index=True)
    descripcion: str | None = Field(default=None, max_length=255)
    activa: bool = Field(default=True)
    area_id: int = Field(foreign_key="area.id")

    area: "Area" = Relationship(back_populates="celulas")
    ejecuciones_auditoria: list["EjecucionAuditoria"] = Relationship(
        back_populates="celula",
    )
