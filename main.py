from helpers.device_manager import DeviceManager
from helpers.image_processor import ImageProcessor
from actions.tap_action import ActionManager
import time

def main():
    device_manager = DeviceManager()
    image_processor = ImageProcessor()

    ActionManager.tap_search_bar(device_manager, image_processor)
    time.sleep(0.3)
    DeviceManager.input_text(device_manager, '3*')

    print('Done')

if __name__ == "__main__":
    main()
