import time

last_click = 0

def handler(e):
    """Manejador de eventos para evitar múltiples clics en un corto período de tiempo (0.5 segundos).
    """
    global last_click
    now = time.time()

    if now - last_click < 0.5:
        return

    last_click = now