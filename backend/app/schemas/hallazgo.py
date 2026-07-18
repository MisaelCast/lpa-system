from datetime import datetime

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class HallazgoBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    descripcion: str = Field(max_length=1000)


class HallazgoCreate(HallazgoBase):
    respuesta_id: int


class HallazgoUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    descripcion: str | None = Field(default=None, max_length=1000)
    respuesta_id: int | None = None


class HallazgoRead(HallazgoBase):
    id: int
    fecha_creacion: datetime
    respuesta_id: int
