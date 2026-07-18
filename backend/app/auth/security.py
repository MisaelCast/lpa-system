"""Password hashing utilities for authentication-related code."""

from passlib.context import CryptContext


_password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Return a bcrypt hash for the provided plain-text password."""
    return _password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against a previously generated hash."""
    return _password_context.verify(password, hashed_password)
