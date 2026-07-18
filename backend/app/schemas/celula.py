from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class CelulaBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str = Field(max_length=150)
    descripcion: str | None = Field(default=None, max_length=255)
    activa: bool = Field(default=True)


class CelulaCreate(CelulaBase):
    area_id: int


class CelulaUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str | None = Field(default=None, max_length=150)
    descripcion: str | None = Field(default=None, max_length=255)
    activa: bool | None = None
    area_id: int | None = None


class CelulaRead(CelulaBase):
    id: int
    area_id: int
