from helpers.device_manager import DeviceManager
from helpers.image_processor import ImageProcessor

class ActionManager:
    @staticmethod
    def tap_ok_button (device_manager: DeviceManager, image_processor: ImageProcessor):
        image = device_manager.take_screenshot()
        ok_coords = image_processor.find_by_text(image, 'ok')
        if ok_coords:
            device_manager.tap(*ok_coords)
        else:
            print('OK button not found')
            return

    @staticmethod
    def tap_search_bar (device_manager: DeviceManager, image_processor: ImageProcessor):
        image = device_manager.take_screenshot()
        search_coords = image_processor.find_by_text(image, 'search')
        if search_coords:
            device_manager.tap(*search_coords)
        else:
            print('Search not found')
            return

