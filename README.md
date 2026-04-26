# MindGames

## Backend Setup

Use the project virtual environment, install the dependencies, then run the backend:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python backend/app.py
```

The backend listens on `0.0.0.0:5000`, so it can be reached from other devices on the same network.

> Important: Open the frontend from the same host IP (for example `http://<host-ip>:5500/index.html`) rather than a local `file://` path. The browser uses the page host to connect to the backend.
