from helpers.device_manager import DeviceManager
from helpers.image_processor import ImageProcessor
from helpers.action_manager import ActionManager
from helpers.location_cache import LocationCache
import time

def main():
    # Setup
    device_manager = DeviceManager()
    image_processor = ImageProcessor()
    location_cache = LocationCache(device_manager, image_processor)

    # Actions

    ActionManager.tap_button(location_cache, "search")
    time.sleep(0.5)
    ActionManager.write_text(location_cache, "3*&!traded")
    time.sleep(0.5)
    ActionManager.tap_button(location_cache, "search")
    time.sleep(0.5)
    device_manager.tap(275, 700) # Select the first pokemon
    time.sleep(0.5)
    ActionManager.tap_button(location_cache, "menu")
    time.sleep(0.5)
    ActionManager.tap_button(location_cache, "appraise")
    time.sleep(0.5)
    ActionManager.tap_button(location_cache, "appraise")
    time.sleep(1)

    print('Done')

if __name__ == "__main__":
    main()
