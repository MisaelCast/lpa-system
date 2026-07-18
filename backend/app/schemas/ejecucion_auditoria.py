from datetime import datetime

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class EjecucionAuditoriaBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    fecha: datetime = Field(default_factory=datetime.utcnow)
    observaciones: str | None = Field(default=None, max_length=1000)


class EjecucionAuditoriaCreate(EjecucionAuditoriaBase):
    auditoria_id: int
    usuario_id: int
    celula_id: int | None = None


class EjecucionAuditoriaUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    fecha: datetime | None = None
    observaciones: str | None = Field(default=None, max_length=1000)
    auditoria_id: int | None = None
    usuario_id: int | None = None
    celula_id: int | None = None


class EjecucionAuditoriaRead(EjecucionAuditoriaBase):
    id: int
    auditoria_id: int
    usuario_id: int
    celula_id: int | None = None
