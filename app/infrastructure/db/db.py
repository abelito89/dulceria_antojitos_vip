import sqlite3
from importlib import resources  # 👈 NUEVO
from ...services.ruta_datos_app import get_app_data_path


DB_PATH = get_app_data_path() / "dulceria.db"


def load_schema_sql() -> str:
    """Carga el schema.sql desde el paquete (compatible con APK)."""
    with resources.files("app.infraestructure.db").joinpath("schema.sql").open("r", encoding="utf-8") as f:
        return f.read()

def get_connection() -> sqlite3.Connection:
    """Crea una conexión a la base de datos SQLite y activa las claves foráneas.

    Returns:
        sqlite3.Connection: Una conexión a la base de datos SQLite con claves foráneas activadas.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)  # 👈 NUEVO
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # IMPORTANTE: activar claves foráneas
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn


def init_db() -> None:
    """Inicializa la base de datos SOLO si no existe."""
    if DB_PATH.exists():
        return

    conn = get_connection()

    schema_sql = load_schema_sql()
    conn.executescript(schema_sql)

    conn.commit()
    conn.close()