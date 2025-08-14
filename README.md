# Site pessoal (Flask) – Gustavo Franco

Site simples com Flask hospedável no Render: Home, Projetos e um placeholder para o Agregador de Notícias Cripto.

## Rodar localmente
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Acesse: http://localhost:5000

## Deploy no Render
1. Suba este código em um repositório no GitHub.
2. No Render: **New + → Web Service** → conecte seu repo.
3. Runtime: Python. Build: `pip install -r requirements.txt`. Start: `gunicorn app:app`.
4. Deploy.
