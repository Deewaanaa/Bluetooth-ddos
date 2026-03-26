import asyncio
from bleak import BleakScanner

async def run():
    print("--- Scanning for Bluetooth Devices (10s) ---")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"Name: {d.name} | MAC: {d.address}")
    print("--- Scan Complete ---")

if __name__ == "__main__":
    asyncio.run(run())
