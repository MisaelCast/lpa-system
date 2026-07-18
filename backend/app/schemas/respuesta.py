from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class RespuestaBase(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    valor: str = Field(max_length=20)
    observaciones: str | None = Field(default=None, max_length=1000)


class RespuestaCreate(RespuestaBase):
    ejecucion_auditoria_id: int
    criterio_id: int


class RespuestaUpdate(SQLModel):
    model_config = ConfigDict(from_attributes=True)

    valor: str | None = Field(default=None, max_length=20)
    observaciones: str | None = Field(default=None, max_length=1000)
    ejecucion_auditoria_id: int | None = None
    criterio_id: int | None = None


class RespuestaRead(RespuestaBase):
    id: int
    ejecucion_auditoria_id: int
    criterio_id: int
