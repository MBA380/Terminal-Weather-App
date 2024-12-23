import os

API_FILE = "API.txt"


def promptApi():
    """
    Prompts the user for an API key at program startup and saves it to a file.
    """
    if not os.path.exists(API_FILE):
        print("Welcome to the Weather App!")
        print("It looks like you're running this for the first time.")
        api_key = input("Please enter your OpenWeatherMap API key: ").strip()

        with open(API_FILE, "w") as file:
            file.write(api_key)
        print("Your API key has been saved.")
    else:
        print("API key file already exists. The application will use the existing key.")


def getApi():
    """
    Retrieves the API key from the file.
    Returns:
        str: The API key.
    """
    if os.path.exists(API_FILE):
        with open(API_FILE, "r") as file:
            return file.read().strip()
    else:
        raise FileNotFoundError(
            "API key file not found. Please restart the application."
        )
