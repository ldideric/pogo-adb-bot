from helpers.location_cache import LocationCache
from helpers.device_manager import DeviceManager

class ActionManager:
    @staticmethod
    def tap_button(location_cache: LocationCache, button_name: str):
        button_coords = None

        if button_name == "menu":
            button_coords = location_cache.get_menu_bar()
        else:
            button_coords = location_cache.get_location_by_text(button_name)

        if button_coords:
            location_cache.device_manager.tap(*button_coords)
        else:
            raise RuntimeError(f"{button_name.capitalize()} button not found")

    @staticmethod
    def write_text(location_cache: LocationCache, text: str):
        location_cache.device_manager.input_text(text)
