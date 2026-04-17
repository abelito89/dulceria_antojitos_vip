$root = Get-Location

Remove-Item -Recurse -Force app\build -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force app\.dart_tool -ErrorAction SilentlyContinue

Set-Location app
flet build apk --module-name main

Set-Location $root