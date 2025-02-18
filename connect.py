import evdev
                        #E4 17 D8 1A 87 0E mac adress 8bitdo
# Detect all input devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
controller = None

# Find the controller
for device in devices:
    print(f"Found device: {device.path} - {device.name}")
    if "controller" in device.name.lower() or "gamepad" in device.name.lower():
        controller = evdev.InputDevice(device.path)
        print(f"Using controller: {controller.name}")
        break

if not controller:
    print("No controller found! Make sure it's connected.")
    exit()

# Read inputs from the controller
print("Reading controller inputs...")

for event in controller.read_loop():
    if event.type == evdev.ecodes.EV_KEY:  # Button presses
        button = evdev.ecodes.KEY[event.code]
        if event.value == 1:  # Button pressed
            print(f"Button Pressed: {button}")
        elif event.value == 0:  # Button released
            print(f"Button Released: {button}")

    elif event.type == evdev.ecodes.EV_ABS:  # Joystick movements
        axis = evdev.ecodes.ABS[event.code]
        value = event.value
        print(f"Joystick Moved: {axis} - Value: {value}")
