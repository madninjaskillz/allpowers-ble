import asyncio
import logging

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from models import AllpowersState

from allpowers_ble import AllpowersBLE

_LOGGER = logging.getLogger(__name__)

ADDRESS = "2A:02:01:59:61:24"


async def run() -> None:
    """Harness to test the device."""
    scanner = BleakScanner()
    future: asyncio.Future[BLEDevice] = asyncio.Future()

    def on_detected(device: BLEDevice, adv: AdvertisementData) -> None:
        if future.done():
            return
        _LOGGER.info("Detected: %s", device)
        if device.address.lower() == ADDRESS.lower():
            _LOGGER.info("Found device: %s", device.address)
            future.set_result(device)

    scanner.register_detection_callback(on_detected)
    await scanner.start()

    def on_state_changed(state: AllpowersState) -> None:
        _LOGGER.info("State changed: %s", state)

    device = await future
    allpowers_device: AllpowersBLE = AllpowersBLE(device)

    cancel_callback = allpowers_device.register_callback(on_state_changed)
    await allpowers_device.initialise()
    torch: bool = True
    for x in range(1, 10):
        _LOGGER.info("loop: " + str(x))
        torch = not torch
        await allpowers_device.set_torch(torch)
        await asyncio.sleep(1)

    cancel_callback()
    await scanner.stop()


logging.basicConfig(level=logging.INFO)
logging.getLogger("allpowersdevice").setLevel(logging.DEBUG)
asyncio.run(run())
