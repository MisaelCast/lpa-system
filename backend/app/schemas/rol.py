from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class RolBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str = Field(max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)


class RolCreate(RolBase):
    pass


class RolUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    nombre: str | None = Field(default=None, max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)


class RolRead(RolBase):
    id: int
