import adafruit_ble
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Initialize the BLE radio
ble = adafruit_ble.BLERadio()
ble.name = "seashark"  # Set the device name

# Create the UART service for communication
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)

# Start advertising the BLE device
ble.start_advertising(advertisement)
print("Advertising as 'seashark'...")

# Keep running to maintain advertisement
while True:
    if ble.connected:
        print("Device connected!")
        while ble.connected:
            pass  # Keep running while connected
    else:
        print("Device disconnected. Restarting advertising...")
        ble.start_advertising(advertisement)
