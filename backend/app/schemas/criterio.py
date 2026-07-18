from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class CriterioBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    descripcion: str = Field(max_length=500)
    orden: int = Field(default=1, ge=1)
    activo: bool = Field(default=True)


class CriterioCreate(CriterioBase):
    auditoria_id: int


class CriterioUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    descripcion: str | None = Field(default=None, max_length=500)
    orden: int | None = Field(default=None, ge=1)
    activo: bool | None = None
    auditoria_id: int | None = None


class CriterioRead(CriterioBase):
    id: int
    auditoria_id: int
