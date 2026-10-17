# orders-api

Order management API for the warehouse system.

```
python -m venv .venv
.venv/bin/pip install -r requirements-dev.txt   # Windows: .venv\Scripts\pip
uvicorn orders_api.main:app --reload
pytest
```
