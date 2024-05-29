# FastAPI

### Ejecutar proyectos

```
uvicorn src.main:app --reload

uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### dependencias

```
pip freeze > requirements.txt

pip freeze > requirements-dev.txt

pip install -r requirements.txt
```