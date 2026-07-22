"""Authorization dependencies based on user roles."""

from fastapi import Depends, HTTPException, status

from app.auth.dependencies import get_current_active_user
from app.models.usuario import Usuario


def require_roles(*roles: str):
    """Factory that returns a dependency enforcing one or more role names.

    Args:
        *roles: One or more role names that are permitted to access the
            endpoint (e.g. ``"Administrador"``, ``"Supervisor"``).

    Returns:
        A FastAPI dependency that validates the authenticated user's role
        and raises HTTP 403 if the role is not in the allowed list.
    """

    def check_role(
        current_user: Usuario = Depends(get_current_active_user),
    ) -> Usuario:
        if current_user.rol.nombre not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tiene permisos suficientes para realizar esta acción.",
            )
        return current_user

    return check_role
