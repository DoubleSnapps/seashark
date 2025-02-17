import time
import board
import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Create the BLE radio object
ble = adafruit_ble.BLERadio()

# Set the device name (appears when scanning)
ble.name = "seashark"

# Create a UART Service (like a serial terminal over Bluetooth)
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)

print("Starting Bluetooth advertisement...")

while True:
    # Start advertising
    ble.start_advertising(advertisement)
    
    # Wait for a connection
    while not ble.connected:
        time.sleep(0.5)

    print("Connection Found")

    while ble.connected:
        # Keep the connection alive
        if uart_service.in_waiting:
            data = uart_service.read(uart_service.in_waiting)
            print(f"Received: {data}")

    print("Disconnected, restarting advertisement...")
