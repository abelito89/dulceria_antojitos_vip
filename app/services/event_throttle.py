import time

last_click = 0

def handler(e):
    global last_click
    now = time.time()

    if now - last_click < 0.5:
        return

    last_click = now