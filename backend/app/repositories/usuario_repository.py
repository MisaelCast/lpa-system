"""Repositorio para la entidad Usuario."""

from sqlmodel import Session, select

from app.models.usuario import Usuario


class UsuarioRepository:
    """Acceso a datos para la tabla ``usuario``."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def obtener_por_id(self, usuario_id: int) -> Usuario | None:
        """Busca un usuario por su identificador único.

        Args:
            usuario_id: ID de la base de datos.

        Returns:
            Instancia de :class:`Usuario` o ``None`` si no se encuentra.
        """
        return self._session.exec(
            select(Usuario).where(Usuario.id == usuario_id)
        ).first()

    def obtener_por_correo(self, correo: str) -> Usuario | None:
        """Busca un usuario por su dirección de correo electrónico.

        Args:
            correo: Correo del usuario (único en el sistema).

        Returns:
            Instancia de :class:`Usuario` o ``None`` si no se encuentra.
        """
        return self._session.exec(
            select(Usuario).where(Usuario.correo == correo)
        ).first()

    def listar(self, skip: int = 0, limit: int = 100) -> list[Usuario]:
        """Lista usuarios con paginación básica.

        Args:
            skip: Registros a omitir (offset).
            limit: Máximo de registros a devolver.

        Returns:
            Lista de instancias de :class:`Usuario`.
        """
        return list(
            self._session.exec(
                select(Usuario).offset(skip).limit(limit)
            ).all()
        )

    def crear(self, usuario: Usuario) -> Usuario:
        """Inserta un nuevo usuario en la base de datos.

        Args:
            usuario: Instancia de :class:`Usuario` lista para persistir.

        Returns:
            La misma instancia con su ID asignado tras el commit.
        """
        self._session.add(usuario)
        self._session.commit()
        self._session.refresh(usuario)
        return usuario

    def actualizar(self, usuario: Usuario) -> Usuario:
        """Actualiza los datos de un usuario existente.

        Args:
            usuario: Instancia de :class:`Usuario` con los cambios deseados.

        Returns:
            La instancia actualizada tras el commit.
        """
        self._session.merge(usuario)
        self._session.commit()
        self._session.refresh(usuario)
        return usuario

    def eliminar(self, usuario: Usuario) -> None:
        """Elimina un usuario de la base de datos.

        Args:
            usuario: Instancia de :class:`Usuario` a eliminar.
        """
        self._session.delete(usuario)
        self._session.commit()
