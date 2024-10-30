1. Crear el virtual environment
`python -m venv .venv`
2. Activar el virtual environment
`.venv\Scripts\Activate.ps1`
3. Instalar pip
`python -m pip install --upgrade pip`
4. Instalar fastapi
`pip install "fastapi[standard]"`
5. Crear archivo requirements.txt
`python -m pip freeze > requirements.txt`
6. creamos el main.py
7. Corremos el servidor 
`fastapi dev main.py`
8. Instalar TestClient
`pip install httpx`
9. Instalar Pytest
`pip install pytest`