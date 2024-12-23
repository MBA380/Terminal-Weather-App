"""
Problem Statement:
Create a terminal-based weather application that allows users to retrieve real-time weather data for any city using the OpenWeatherMap API. The application should allow the user to input a city name and retrieve detailed and concise weather information for the entered city. Furthermore, the application should be easy to use and also allow users the ability to change their API keys easily.

To solve the problem, this application uses the curses library to create an intuitive terminal-based interface for easy navigation, data entry, and clean data display. Additionally, it utilizes the built-in OS library for file management, and the urllib library to fetch weather data as a JSON response.
"""

import curses
from curses import wrapper

import weather  # Handles weather fetching and display
from api import promptApi  # Updated API key management

menuOptions = ["Check Weather", "Select Temperature Unit", "Change API Key", "Exit"]


def printMenu(stdscr, currentRow):
    """
    Displays the main menu with options and navigational instructions.

    Args:
        stdscr: The curses screen object for terminal input/output.
        currentRow: The currently selected menu option (used for highlighting).
    """
    stdscr.clear()  # Clears the curses buffer, resetting it to a blank state
    h, w = stdscr.getmaxyx()  # Gets the max X and Y coordinates of the users terminal

    # Loop through menu options and print them, highlighting the current selection
    for index, row in enumerate(menuOptions):
        x = (
            w // 2 - len(row) // 2
        )  # Ensures the X and Y coordinates are centered to the terminal
        y = h // 2 - len(menuOptions) // 2 + index
        if index == currentRow:
            stdscr.attron(curses.color_pair(1))  # Turns on color for future output
            stdscr.addstr(y, x, row)  # Prints the row (from menuOptions) at x and y
            stdscr.attroff(curses.color_pair(1))  # Turns off color highlighting
        else:
            stdscr.addstr(y, x, row)

    # Display instructions and a welcome message above the menu
    welcomeStr = "Welcome to the Weather App! Choose an option below:"
    selectStr = "(Use arrow keys to navigate and Enter to select)"
    yBase = h // 2 - len(menuOptions) - 3
    stdscr.addstr(yBase, w // 2 - len(welcomeStr) // 2, welcomeStr)
    stdscr.addstr(yBase + 2, w // 2 - len(selectStr) // 2, selectStr)
    stdscr.refresh()  # Pushes the buffer in curses to the user


def changeApiKey(stdscr):
    """
    Prompts the user to update the API key using the curses interface.

    Args:
        stdscr: The curses screen object for terminal input/output.
    """
    stdscr.clear()
    stdscr.addstr(1, 1, "Enter a new API key: ")
    curses.echo()  # Enable echo for user input
    new_api_key = stdscr.getstr(2, 1, 40).decode("utf-8").strip()
    curses.noecho()  # Disable echo after input

    if new_api_key:
        with open("API.txt", "w") as file:
            file.write(new_api_key)
        stdscr.addstr(4, 1, "API Key updated successfully.")
    else:
        stdscr.addstr(4, 1, "API Key update canceled. Using existing key.")

    stdscr.addstr(6, 1, "Press any key to return to the menu.")
    stdscr.refresh()
    stdscr.getch()


def main(stdscr):
    """
    Main function to manage the terminal interface and menu navigation.
    """
    curses.curs_set(0)  # Hide terminal cursor
    curses.init_pair(  # Enable color pairs for highlighting
        1, curses.COLOR_BLACK, curses.COLOR_WHITE
    )
    currentRow = 0  # Start at the first item in menuOption

    tempUnit = "metric"  # Sets default temp unit as celsius

    while True:
        printMenu(stdscr, currentRow)
        key = stdscr.getch()

        # Navigate menu options
        if key == curses.KEY_UP and currentRow > 0:
            currentRow -= 1
        elif key == curses.KEY_DOWN and currentRow < len(menuOptions) - 1:
            currentRow += 1
        elif key in [10, 13]:  # Enter key
            stdscr.clear()
            if menuOptions[currentRow] == "Check Weather":
                weather.weatherMain(stdscr, tempUnit)  # Pass tempUnit to weather module
            elif menuOptions[currentRow] == "Select Temperature Unit":
                tempUnit = weather.selectTempUnit(stdscr)  # Update temp unit
            elif menuOptions[currentRow] == "Change API Key":
                changeApiKey(stdscr)  # Handle API key change
            elif menuOptions[currentRow] == "Exit":
                break


def setup():
    """
    Setup function to initialize the application by prompting for the API key.
    """
    promptApi()


# Start the program:
if (  # This checks if code is run directly and not being imported as a module
    __name__ == "__main__"
):
    setup()  # Prompt for API key at startup
    wrapper(  # Sets up the terminal in curses mode and passes the stdscr object to the "main" function
        main
    )
