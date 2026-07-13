from sqlmodel import Field, SQLModel


class HallazgoResponsable(SQLModel, table=True):
    """Relaciona hallazgos con los usuarios responsables de atenderlos."""

    __tablename__ = "hallazgo_responsable"

    hallazgo_id: int = Field(foreign_key="hallazgo.id", primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)
