import keyboard

last_key = None

def on_key(event):
    global last_key
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == last_key:
            return
        else:
            print(event.name)
            last_key = event.name

keyboard.on_press(on_key)
keyboard.wait('esc')