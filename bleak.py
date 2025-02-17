import asyncio
import logging
from bleak import BleakAdvertiser

# Set up logging
logging.basicConfig(level=logging.INFO)

async def advertise():
    advertiser = BleakAdvertiser()
    advertisement_data = {
        "local_name": "PiZeroW_BLE",
        "manufacturer_data": {0xFFFF: b"RPiZero"},
        "service_uuids": ["12345678-1234-5678-1234-56789abcdef0"]
    }
    
    logging.info("Starting BLE advertisement on Raspberry Pi Zero W...")
    async with advertiser:
        await advertiser.start(**advertisement_data)
        while True:
            await asyncio.sleep(10)  # Keep advertising indefinitely

if __name__ == "__main__":
    try:
        asyncio.run(advertise())
    except KeyboardInterrupt:
        logging.info("BLE advertisement stopped.")
