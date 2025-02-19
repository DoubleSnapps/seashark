import evdev

# List all devices
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
print("🔍 Detected input devices:")
for device in devices:
    print(f"📌 {device.path} - {device.name}")

# Try to find the 8BitDo controller
controller = None
for device in devices:
    if "8bitdo" in device.name.lower() or "gamepad" in device.name.lower() or "controller" in device.name.lower():
        controller = evdev.InputDevice(device.path)
        print(f"✅ Using controller: {controller.name} (Device Path: {device.path})")
        break

if not controller:
    print("❌ No controller found! Make sure it's connected.")
    exit()

# Read inputs
print("🎮 Listening for controller inputs...")
for event in controller.read_loop():
    if event.type == evdev.ecodes.EV_KEY:  # Button presses
        button = evdev.ecodes.KEY.get(event.code, f"Unknown Button {event.code}")  # Prevent crash
        if event.value == 1:  # Button pressed
            print(f"🚀 Button Pressed: {button}")
        elif event.value == 0:  # Button released
            print(f"🛑 Button Released: {button}")

    elif event.type == evdev.ecodes.EV_ABS:  # Joystick movements
        axis = evdev.ecodes.ABS.get(event.code, f"Unknown Axis {event.code}")  # Prevent crash
        value = event.value
        print(f"🎯 Joystick Moved: {axis} - Value: {value}")
