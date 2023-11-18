from ppadb.client import Client
import os
import io
from PIL import Image

class DeviceManager:
    def __init__(self, host='127.0.0.1', port=5037):
        self.adb = Client(host=host, port=port)
        self.device = self._get_device()

    def _get_device(self):
        devices = self.adb.devices()
        if len(devices) == 0:
            raise RuntimeError('No device attached')
        return devices[0]

    def take_screenshot(self, save_path='./img/screenshot.png'):
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))

        image = Image.open(io.BytesIO(self.device.screencap()))
        image.save(save_path)
        return image

    def tap(self, x, y):
        self.device.shell(f"input tap {x} {y}")

    def input_text(self, text):
        self.device.shell(f"input text '{text}'")
