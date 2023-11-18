from helpers.device_manager import DeviceManager
from helpers.image_processor import ImageProcessor

class LocationCache:
    def __init__(self, device_manager: DeviceManager, image_processor: ImageProcessor):
        self.cache = {}
        self.device_manager = device_manager
        self.image_processor = image_processor

    def get_location_by_text(self, text):
        if text in self.cache:
            return self.cache[text]
        else:
            image = self.device_manager.take_screenshot()
            location = self.image_processor.find_by_text(image, text)
            self.cache[text] = location
            return location

    def get_menu_bar(self):
        if 'menu_bar' in self.cache:
            return self.cache['menu_bar']
        else:
            image = self.device_manager.take_screenshot()
            screen_width, screen_height = self.get_screen_size()
            search_line = int(screen_width * 7 / 8)
            color = "#95fbb5"  # Color of the hamburger menu bar
            found_coords = None
            for x in range(screen_width):
                pixel_color = self.image_processor.get_pixel_color(image, x, search_line)
                if pixel_color == color:
                    found_coords = (x, search_line)
                    break
            self.cache['menu_bar'] = found_coords
            return found_coords

    def get_screen_size(self):
        if 'screen_size' in self.cache:
            return self.cache['screen_size']
        else:
            image = self.device_manager.take_screenshot()
            screen_size = self.image_processor.get_screen_size(image)
            self.cache['screen_size'] = screen_size
            return screen_size
