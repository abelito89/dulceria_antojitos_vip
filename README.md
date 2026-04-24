# Angelica — Aplicación Flet (versión actual) que calcula costos de productos elaborados en dulcería.

Resumen
- Aplicación de escritorio/móvil creada con Flet (v0.84).
- Proyecto estructurado en Python con UI en `app/ui` y lógica de dominio en `app/domain`.

Requisitos (versiones detectadas en este equipo)
- Java (OpenJDK): openjdk version "17.0.13" (Temurin-17.0.13+11)
- Javac: `javac 17.0.13`
- Flutter: `Flutter 3.41.4` (Framework revision ff37bef603, Dart 3.11.1)
- Android SDK: `C:\Users\iviso\AppData\Local\Android\Sdk`
- Android NDK: `20.0` (variable de entorno `ANDROID_NDK_ROOT` = 20.0)
- Android Debug Bridge (adb): `Android Debug Bridge version 1.0.41` (platform-tools Version 37.0.0-14910828)
- Gradle (global): no se encontró un `gradle` global en PATH — puede usarse el wrapper del proyecto o instalar Gradle si se requiere.

Nota: estas versiones se obtuvieron ejecutando los comandos del sistema en este equipo; si trabajas desde otra máquina, verifica las versiones locales.

Requisitos adicionales
- Python 3.10+ (se recomienda usar un entorno virtual).
- Flet 0.84 (ver `requirements.txt`).

Instalación y ejecución rápida (entorno de desarrollo)
1. Crear y activar entorno virtual:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Instalar dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

3. Ejecutar la app (desde la carpeta `app`):

   ```powershell
   cd app
   py main.py
   ```

Generar APK (build)
- Para crear el APK desde la misma ubicación (`app`) usa:

   ```powershell
   flet build apk --module-name main
   ```

- El script `app/compilar.ps1` incluye pasos para limpiar y ejecutar `flet build apk --module-name main`.

Estructura principal (resumen)
- `app/main.py`: punto de entrada de la aplicación.
- `app/ui/`: vistas, componentes y callbacks de la interfaz.
- `app/ui/components`: componentes reutilizables (ej.: `crear_item_materia_prima.py`).
- `app/domain/`, `app/services/`, `app/infrastructure/`: lógica de negocio y persistencia.
- `state/receta_context.py`: gestión de estado central (contextos y estados compartidos).

Dónde mirar primero
- Interfaz y callbacks: [app/ui/callbacks.py](app/ui/callbacks.py)
- Vistas: [app/ui/views/recetas_view.py](app/ui/views/recetas_view.py) y otras en `app/ui/views`.
- Gestión de estado: [state/receta_context.py](state/receta_context.py)

Backend y base de datos (SQLite)
- Motor: SQLite embebido usado por los repositorios en `app/infrastructure/db/repositories/*`.
- Archivo de esquema: `app/infrastructure/db/schema.sql` — contiene tablas `materia_prima`, `lotes`, `receta`, `receta_ingrediente` y los índices principales.
- Inicialización: `app/infrastructure/db/db.py` expone `set_db_path()`, `init_db()` y `get_connection()`.
   - Al iniciar la app `app/main.py` crea un directorio `dulceria` dentro de la ruta base del sistema y llama a `set_db_path(data_dir)` y `init_db()`.

Rutas donde se crea el archivo `.db` (ejemplos)
- Android (APK, app internal storage):
   - Base detectada en `main.py`: `/data/user/0/com.flet.app/files`
   - Directorio de aplicación usado: `/data/user/0/com.flet.app/files/dulceria`
   - Archivo final: `/data/user/0/com.flet.app/files/dulceria/dulceria.db`
- Windows (desarrollo local):
   - Base detectada: `%USERPROFILE%\AppData\Local`
   - Archivo final (ejemplo): `C:\Users\<usuario>\AppData\Local\dulceria\dulceria.db`
- Linux / macOS (desarrollo local):
   - Base detectada: `~/.local/share`
   - Archivo final (ejemplo): `/home/<usuario>/.local/share/dulceria/dulceria.db`

Justificación de las elecciones de ruta y diseño
- Uso de directorios de aplicación (internos) — motivo:
   - Portabilidad y coherencia: las rutas elegidas siguen convenciones por plataforma para datos de aplicación (no mezclan directorios temporales ni rutas públicas).
   - Sin permisos adicionales en Android: almacenar en el directorio interno de la app evita requerir permisos de almacenamiento externo y reduce problemas de compatibilidad con cambios en políticas de Android 10/11+.
   - Seguridad y aislamiento: archivos internos están protegidos por el sistema (otros apps no pueden acceder sin permisos/root).
- Uso de SQLite embebido — motivo:
   - Sencillez y dependencia mínima: SQLite está incluida con Python y no requiere servidor.
   - Suficiente para el alcance de la app: datos relacionales simples, índices y constraints (CHECK, UNIQUE, FK) se aprovechan en `schema.sql`.
   - Fácil export/import para backups y debugging.

Detalles técnicos importantes
- Schema y restricciones: `schema.sql` activa `PRAGMA foreign_keys = ON;` y declara CHECKs y UNIQUEs para mantener integridad en la base.
- Conexiones: `get_connection()` aplica `conn.row_factory = sqlite3.Row` y `PRAGMA foreign_keys = ON;` para consistencia.
- Inicialización: `init_db()` crea las tablas si no existen, y emite la ruta `DB PATH:` en stdout para depuración.
- Empaquetado: `load_schema_sql()` carga `schema.sql` como recurso del paquete, esto funciona tanto en entorno de desarrollo como dentro del APK.

Permisos y consideraciones Android
- Al usar almacenamiento interno (`/data/user/0/.../files`) la app NO necesita permisos de almacenamiento (no requiere `WRITE_EXTERNAL_STORAGE` ni `MANAGE_EXTERNAL_STORAGE`).
- Si decides permitir exportar/importar la DB a almacenamiento público (SD o directorio compartido) deberás:
   - Añadir permisos en `AndroidManifest.xml` (cuando sea necesario):
      - `android.permission.WRITE_EXTERNAL_STORAGE` (antiguo/limitado en Android 10+)
      - Para Android 11+ usar el API de `MediaStore` o solicitar `MANAGE_EXTERNAL_STORAGE` (permiso de alto riesgo, mala experiencia y revisión adicional en Play Store).
   - Implementar flujo de permisos en tiempo de ejecución y manejar el caso en que el usuario deniegue el permiso.
   - Preferible: implementar exportación a través de la UI (guardar a `StoragePaths().get_application_documents_directory` o pedir al usuario una carpeta mediante un file picker) para evitar necesitar permisos globales.

Inspección/backup del archivo DB en Android (formas seguras)
- Recomendado: implementar en la app una función `Exportar` que copie `dulceria.db` a una ubicación accesible (por ejemplo, un folder elegido por el usuario) o que genere un archivo `.zip` descargable.
- Línea de comandos (requiere que la app sea debuggable o root):
   - Usando `adb run-as` (app debuggable):

      ```powershell
      adb shell "run-as com.flet.app cat files/dulceria/dulceria.db" > dulceria.db
      ```

   - Si la app no es debuggable, necesitarás usar métodos de exportación dentro de la app o acceso root al dispositivo.

Buenas prácticas operativas
- No escribas la DB desde múltiples procesos simultáneos sin control: SQLite maneja concurrencia limitada — la app centraliza acceso con `get_connection()` y operaciones rápidas/atómicas.
- Realiza backups periódicos: exportar JSON o copia de la DB antes de migraciones.
- Añade migraciones si cambias schema: no sobrescribas el archivo con un nuevo schema sin migrar datos reales.


Notas para desarrolladores
- Este repositorio fue creado con Flet 0.84 — usa esa versión para evitar incompatibilidades.
- Si necesitas compilar para Android y faltan herramientas, instala Android SDK (y NDK si se requiere), y añade `platform-tools` y `tools/bin` al PATH.
- Gradle puede no estar instalado globalmente en este equipo; Flutter normalmente usa su propio wrapper.

Contacto
- Si surge una duda sobre la arquitectura, revisa primero los archivos indicados y luego contacta al responsable del proyecto.
