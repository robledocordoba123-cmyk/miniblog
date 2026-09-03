# MiniBlog en Contenedores

Proyecto desarrollado como actividad práctica del módulo **DevOps y Contenedores** del programa Tecnólogo en Análisis y Desarrollo de Software (ADSO) – SENA, CTMA, ficha 3229209.

## Descripción

Aplicación web mínima construida con **Flask** (Python) y conectada a una base de datos **PostgreSQL**, containerizada con Docker y orquestada con Docker Compose. El proyecto incluye control de versiones con Git/GitHub y un pipeline de integración continua (CI) con GitHub Actions.

## Tecnologías usadas

- Python (Flask)
- PostgreSQL
- Docker y Docker Compose
- Git y GitHub
- GitHub Actions (CI/CD)

## Estructura del proyecto

- `app.py` — aplicación Flask
- `Dockerfile` — receta para construir la imagen de la app
- `docker-compose.yml` — orquesta los servicios web y db
- `requirements.txt` — dependencias de Python
- `test_app.py` — pruebas unitarias
- `.github/workflows/ci.yml` — pipeline de integración continua
- `docs/` — documentación de la actividad (evidencias)

## Cómo ejecutar el proyecto

```bash
docker compose up -d
```

La aplicación queda disponible en `http://localhost:8080` (o el puerto configurado en `docker-compose.yml`).

## Autora

Manuela Córdoba Robledo — Aprendiz ADSO, SENA
