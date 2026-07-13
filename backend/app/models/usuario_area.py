from sqlmodel import Field, SQLModel


class UsuarioArea(SQLModel, table=True):
    """Asigna usuarios a las areas donde pueden operar."""

    __tablename__ = "usuario_area"

    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
    area_id: int = Field(foreign_key="area.id", primary_key=True)
