import sqlite3
from importlib import resources
from pathlib import Path


DB_PATH: Path | None = None



def set_db_path(base_path: Path):
    global DB_PATH
    DB_PATH = base_path / "dulceria.db"

def load_schema_sql() -> str:
    """Carga el schema.sql desde el paquete (compatible con APK)."""
    with resources.files("infrastructure.db").joinpath("schema.sql").open("r", encoding="utf-8") as f:
        return f.read()

def get_connection() -> sqlite3.Connection:
    if DB_PATH is None:
        raise RuntimeError("DB_PATH no inicializado. Llama a set_db_path() primero.")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn


def init_db() -> None:
    if DB_PATH is None:
        raise RuntimeError("DB_PATH no inicializado. Llama a set_db_path() primero.")

    conn = get_connection()

    schema_sql = load_schema_sql()
    conn.executescript(schema_sql)

    print("DB PATH:", DB_PATH)

    conn.commit()
    conn.close()