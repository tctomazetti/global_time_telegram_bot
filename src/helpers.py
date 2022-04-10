"""
generic functions to help with the project
"""


def main_menu() -> str:
    """main menu"""
    menu = """
    Choose one of the following options (type the number)
/1. Search by the city name.
/2. Search by the geographic coordinates.

Any other message will be sent to the default answer.
    """
    return menu


def get_weather_by_city(city: str) -> str:
    pass


def get_weather_by_coordinates(coordinates: str) -> str:
    pass
