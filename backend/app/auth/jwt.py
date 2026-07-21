"""JWT token generation and validation utilities."""

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from app.config import settings


def create_access_token(subject: str, expires_delta: timedelta | None = None) -> str:
    """Generate a signed JWT access token for the given subject.

    Args:
        subject: Identifier to store in the ``sub`` claim.
        expires_delta: Optional custom expiration offset. Falls back to
            ``ACCESS_TOKEN_EXPIRE_MINUTES`` when not provided.

    Returns:
        Encoded JWT string.
    """
    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta is not None
        else timedelta(minutes=settings.access_token_expire_minutes)
    )

    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT access token.

    Args:
        token: The encoded JWT string to decode.

    Returns:
        The decoded payload dictionary.

    Raises:
        jwt.ExpiredSignatureError: If the token has expired.
        jwt.InvalidTokenError: If the token signature is invalid or the
            token cannot be parsed.
    """
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )
