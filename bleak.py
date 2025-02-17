from bleak import BleakAdvertiser
import asyncio

async def advertise():
    async with BleakAdvertiser() as advertiser:
        await advertiser.start(name="seashark")
        print("Advertising as 'seashark'...")
        await advertiser.wait_for_stop()

asyncio.run(advertise())
