# Flask Movies MVC App

A simple Flask MVC application that inserts the provided movie dataset into a MongoDB-backed collection and renders it in an HTML table.

## Run

```bash
pip install -r requirements.txt
python app.py
```

The app attempts to use a real MongoDB instance via `MONGODB_URI`, and automatically falls back to `mongomock` if no local server is running.
