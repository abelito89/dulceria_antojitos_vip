import sqlite3
from pathlib import Path
from app.services.ruta_datos_app import get_app_data_path

BASE_DIR = Path(__file__).resolve().parent # Obtener el directorio base del proyecto (app/infraestructure/db)
DB_PATH = get_app_data_path() / "dulceria.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


def get_connection() -> sqlite3.Connection:
    """Crea una conexión a la base de datos SQLite y activa las claves foráneas.

    Returns:
        sqlite3.Connection: Una conexión a la base de datos SQLite con claves foráneas activadas.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # IMPORTANTE: activar claves foráneas
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn


def init_db() -> None:
    """Abre una conexion a la db usando el schema.sql para crear las tablas necesarias.
    """
    conn = get_connection()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    conn.executescript(schema_sql)
    conn.commit()
    conn.close()