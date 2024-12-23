"""
Handles weather data fetching and display.
Provides functionality to:
1. Fetch current weather for a user-specified location.
2. Allow the user to select their preferred temperature unit.
"""

import curses
import json
from urllib.request import urlopen  # Handles API requests

from api import getApi  # Calls getApi to read the API key from file


def weatherMain(stdscr, tempUnit):
    """
    Fetches and displays weather data for a user-specified location.
    Args:
        stdscr: The curses screen object for terminal input/output.
        tempUnit: The temperature unit ('metric', 'imperial', or 'standard').
    """
    stdscr.clear()
    API = getApi()  # Saves the api key to 'API'

    stdscr.addstr(1, 1, "Enter the city name: ")
    curses.echo()  # Enables echo mode for the user to see their input
    city = stdscr.getstr(2, 1, 40).decode("utf-8").strip()
    curses.noecho()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units={tempUnit}"

    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode())

        stdscr.clear()
        stdscr.addstr(1, 1, f"City: {data['name']}")
        stdscr.addstr(2, 1, f"Temperature: {data['main']['temp']}°")
        stdscr.addstr(3, 1, f"Feels Like: {data['main']['feels_like']}°")
        stdscr.addstr(
            4, 1, f"Condition: {data['weather'][0]['description'].capitalize()}"
        )
    except Exception as e:  # Error handling
        stdscr.addstr(6, 1, f"Error: {e}")

    stdscr.addstr(8, 1, "Press any key to return to the menu.")
    stdscr.refresh()
    stdscr.getch()


def selectTempUnit(stdscr):
    """
    Allows the user to select a temperature unit.
    Args:
        stdscr: The curses screen object for terminal input/output.
    Returns:
        str: The selected temperature unit ('metric', 'imperial', or 'standard').
    """
    stdscr.clear()
    options = ["Celsius (Metric)", "Fahrenheit (Imperial)", "Kelvin (Standard)"]
    currentRow = 0

    while True:
        # Uses the same logic as in the printMenu() function for input highlighting
        stdscr.clear()
        for idx, option in enumerate(options):
            x = 2
            y = 2 + idx
            if idx == currentRow:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, option)
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and currentRow > 0:
            currentRow -= 1
        elif key == curses.KEY_DOWN and currentRow < len(options) - 1:
            currentRow += 1
        elif key in [10, 13]:  # Enter key
            return ["metric", "imperial", "standard"][currentRow]
