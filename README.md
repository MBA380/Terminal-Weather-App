# Weather App

A terminal-based weather application that allows users to retrieve real-time weather data for any city using the OpenWeatherMap API. The application is designed for ease of use, featuring intuitive navigation and straightforward data presentation.

## Features

- **Real-Time Weather Data**: Fetch current weather details for any city worldwide.
- **Customizable API Key**: Easily update your OpenWeatherMap API key from within the application.
- **Temperature Units**: Choose between Celsius, Fahrenheit, and Kelvin for weather data.
- **Terminal-Based Interface**: Simple and interactive navigation using arrow keys and a visually appealing menu system.

## Limitations

This project exclusively uses Python's Standard Library due to constraints. As a result, third-party libraries (e.g., `requests`) for handling API requests were not used. Instead, the `urllib` module was utilized to fetch data from the OpenWeatherMap API.

## Getting Started

### Prerequisites

- Python 3.6 or later.
- An OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/) to get one).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MBA380/Terminal-Weather-App.git
   cd Terminal-Weather-App
   ```
2. Install any required dependencies (if applicable).

### Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. On first launch, the program will prompt you to enter your OpenWeatherMap API key. The key will be saved locally in an `API.txt` file for future use.
3. Use the arrow keys to navigate the menu and press Enter to select options.
   - **Check Weather**: Input a city name to view its current weather.
   - **Select Temperature Unit**: Choose your preferred unit for temperature data.
   - **Change API Key**: Update your OpenWeatherMap API key if needed.
   - **Exit**: Close the application.

## File Structure

- `main.py`: Entry point for the application, managing the terminal interface and menu navigation.
- `api.py`: Handles API key management, including saving and retrieving the key from `API.txt`.
- `weather.py`: Fetches weather data from the OpenWeatherMap API and displays it to the user.
- `API.txt`: Stores the OpenWeatherMap API key locally.

## Known Issues

- Ensure that the `API.txt` file is not deleted unless intending to reset the API key.
- Invalid or expired API keys will result in an error when fetching weather data.
