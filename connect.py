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
    print(f"{device.path} - {device.name}")

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
                    print("B: Unbound")
                case "X":
                    print("X: Unbound")
                case "Y":
                    print("Y: Unbound")
                case "LB":
                    print("LB: Unbound")
                case "RB":
                    print("RB: Running Snapshot Command")
                    robot.buzz()
                    capture_image(1000)
                    robot.revbuzz()
                case "-":
                    print("-: Unbound")
                case "+":
                    print("+: Unbound")
                case "MENU":
                    print("MENU: Unbound")
                case _: 
                    print(f"Warning: Unmapped Button: {button}")

        elif event.value == 0:  # Button released
            print(f"Released: {button}")
            robot.stop()

    elif event.type == evdev.ecodes.EV_ABS:  # D-Pad, Triggers, Joysticks
        axis_name = evdev.ecodes.ABS.get(event.code, f"Unknown Axis {event.code}")
        value = event.value
        
        if axis_name in constants.AXIS_MAP and value in constants.AXIS_MAP[axis_name]:
            action = constants.AXIS_MAP[axis_name][value]
            print(f"🎮 {action} Pressed")

            # Handle joystick/D-Pad actions
            match action:
                case "UDpad":
                    print("UDpad: Drive Up")
                    robot.drive(1)
                case "DDpad":
                    print("DDpad: Drive Back")
                    robot.drive(-1)
                case "LDpad":
                    print("LDpad: Drive Left")
                    robot.turnL(1)
                case "RDpad":
                    print("RDpad: Drive Right")
                    robot.turnR(1)
                case "LT":
                    print("LT: Unbound")
                case "RT":
                    print("RT: Unbound")
                case "JU":
                    print("JU: Drive Fowards")
                case "JD":
                    print("JD: Drive Back")
                case "JL":
                    print("JL: Strafing Left")
                case "JR":
                    print("JR: Strafing Right")
                case _:
                    print(f"Warning: Unmapped Axis: {action}")

        # Detect Released Actions (when input returns to neutral state)
        elif axis_name in constants.AXIS_MAP and value == 0:
            print(f"{axis_name} Released - Stopping Movement")

            # Handle axis releases
            match axis_name:
                case "ABS_HAT0X" | "ABS_HAT0Y":
                    robot.stop()
                case "ABS_Z":  # Left Trigger Released
                    print("LT Released")
                case "ABS_RZ":  # Right Trigger Released
                    print("RT Released")
                case "ABS_X" | "ABS_Y":  # Joystick Released
                    robot.stop()
                case _:
                    print(f"Warning: Unkown Axis Release: {axis_name}")