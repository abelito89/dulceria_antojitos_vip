from app.infrastructure.db.db import init_db

def main():
    """Función principal que inicializa la base de datos y muestra un mensaje de confirmación.
    """
    init_db()
    print("Base de datos inicializada")

if __name__ == "__main__":
    main()