# LPA System Backend

Backend base del proyecto LPA System construido con FastAPI.

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

## Ejecutar FastAPI

```bash
uvicorn app.main:app --reload
```

La API quedara disponible en `http://127.0.0.1:8000`.
