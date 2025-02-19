import evdev
from Constants import *
#from capture import capture_image

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
        print(f"Using controller: {controller.name} (Device Path: {device.path})")
        break

if not controller:
    print("ERROR: No controller found!")
    exit()


# Read inputs
print("Listening for controller inputs...")
for event in controller.read_loop():
    if event.type == evdev.ecodes.EV_KEY:  # Button presses
        button = constants.BUTTON_MAP.get(event.code, f"Unknown Button {event.code}")
        if event.value == 1:  # Button pressed
            print(f"🚀 Button Pressed: {button}")

            # Handle button actions with match-case
            match button:
                case "A":
                    print("Button Pressed: A")
                case "B":
                    print("Button Pressed: B")
                case "X":
                    print("Button Pressed: X")
                case "Y":
                    print("Button Pressed: Y")
                case "LB":
                    print("Button Pressed: LB")
                case "RB":
                    print("Button Pressed: RB")
                    print("Running Snapshot Command")
                case "-":
                    print("Button Pressed: -")
                case "+":
                    print("Button Pressed: +")
                case _:
                    print(f"Warning: Unmapped Button: {button}")

        elif event.value == 0:  # Button released
            print(f"Released: {button}")

    elif event.type == evdev.ecodes.EV_ABS:  # Joystick movements
        axis = evdev.ecodes.ABS.get(event.code, f"Unknown Axis {event.code}")
        value = event.value
        print(f"🎯 Joystick Moved: {axis} - Value: {value}")