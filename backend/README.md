# LPA System Backend

Backend base del proyecto LPA System construido con FastAPI.

## Instalar PostgreSQL

En Ubuntu/Debian:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

En macOS con Homebrew:

```bash
brew install postgresql
brew services start postgresql
```

## Crear entorno virtual

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configurar variables de entorno

```bash
cp .env.example .env
```

Edita `.env` con los valores de tu entorno:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=lpa_system
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
```

## Crear base de datos

Con el usuario `postgres`:

```bash
createdb -U postgres lpa_system
```

Tambien puedes crearla desde `psql`:

```sql
CREATE DATABASE lpa_system;
```

## Ejecutar FastAPI

```bash
uvicorn app.main:app --reload
```

La API quedara disponible en `http://127.0.0.1:8000`.
