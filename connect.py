import evdev
from Constants import *
from drivebase import *
from capture import capture_image

# List all devices
robot = Drivebase()
print("Robot Constructed")

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
print("searching")
for device in devices:
    print(f"📌 {device.path} - {device.name}")

controller = None
for device in devices:
    if "8bitdo" in device.name.lower() or "gamepad" in device.name.lower() or "controller" in device.name.lower():
        controller = evdev.InputDevice(device.path)
        print(f"Controller: {controller.name} (Device Path: {device.path})")
        break

if not controller:
    print("ERROR: No controller found!")
    exit()


# Read inputs
print("Listening Started")
for event in controller.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        button = constants.BUTTON_MAP.get(event.code, f"Unknown Button {event.code}")
        if event.value == 1:
            match button:
                case "A":
                    print("A: Drive forward")
                    robot.drive(0.5)
                case "B":
                    print("Button Pressed: B")
                case "X":
                    print("Button Pressed: X")
                case "Y":
                    print("Button Pressed: Y")
                case "LB":
                    print("Button Pressed: LB")
                case "RB":
                    print("RB: Running Snapshot Command")
                    capture_image(1000)
                case "-":
                    print("Button Pressed: -")
                case "+":
                    print("Button Pressed: +")
                case _: 
                    print(f"Warning: Unmapped Button: {button}")

        elif event.value == 0:  # Button released
            print(f"Released: {button}")
            robot.stop()

    elif event.type == evdev.ecodes.EV_ABS:  # Joystick movements
        axis = evdev.ecodes.ABS.get(event.code, f"Unknown Axis {event.code}")
        value = event.value
        print(f"🎯 Joystick Moved: {axis} - Value: {value}")