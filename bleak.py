import os
import time

def start_ble_advertising():
    print("Starting Bluetooth LE Advertisement...")

    # Enable Bluetooth
    os.system("sudo bluetoothctl power on")

    # Set device to advertise mode
    os.system("sudo bluetoothctl advertise on")

    # Set a custom name
    os.system('sudo bluetoothctl system-alias PiZeroW_BLE')

    # Advertise indefinitely
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopping advertisement...")
        os.system("sudo bluetoothctl advertise off")

if __name__ == "__main__":
    start_ble_advertising()
