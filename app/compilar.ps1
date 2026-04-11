# 1. Vincular librerías de Python
$env:SERIOUS_PYTHON_SITE_PACKAGES="$PSScriptRoot\.venv\Lib\site-packages"

# 2. VALIDACIÓN: ¿Existe la carpeta de Android?
if (!(Test-Path "build\flutter\android")) {
    Write-Host "Estructura no encontrada. Generando carpetas con Flet (esto fallará al final, es normal)..." -ForegroundColor Cyan
    # Lanzamos el build normal. Aunque falle por el NDK, dejará las carpetas creadas.
    flet build apk
}

# 3. Entrar a la carpeta de Android (aquí ya debería existir)
if (Test-Path "build\flutter\android") {
    cd build\flutter\android

    Write-Host "Iniciando compilación manual con Gradle..." -ForegroundColor Magenta

    # 4. Compilar el APK
    .\gradlew.bat assembleRelease --offline -P android.ndkVersion="28.2.13676358"

    # 5. Volver a la raíz del proyecto
    cd ..\..\..

    Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
    Write-Host "¡PROCESO TERMINADO!" -ForegroundColor Green
    Write-Host "Busca tu APK en: build\flutter\android\app\build\outputs\apk\release\app-release.apk" -ForegroundColor Yellow
    Write-Host "------------------------------------------------------------" -ForegroundColor Cyan
} else {
    Write-Host "ERROR: No se pudo crear la estructura de carpetas. Revisa que Flet esté instalado." -ForegroundColor Red
}