import requests


# Convert weather codes into readable descriptions
def get_weather_description(code):

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Slight Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Slight Rain Showers",
        81: "Moderate Rain Showers",
        82: "Violent Rain Showers",
        95: "Thunderstorm",
        96: "Thunderstorm with Hail",
        99: "Heavy Thunderstorm with Hail"
    }

    return weather_codes.get(code, "Unknown Weather")


# Find city coordinates
def get_city_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        return None

    location = data["results"][0]

    return {
        "name": location["name"],
        "country": location.get("country", "Unknown"),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


# Fetch weather information
def get_weather(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "weather_code",
            "wind_speed_10m"
        ],
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


# Display weather information
def display_weather(location, weather):

    current = weather["current"]
    units = weather["current_units"]

    description = get_weather_description(
        current["weather_code"]
    )

    print("\n================================")
    print("       WEATHER INFORMATION")
    print("================================")

    print(f"City: {location['name']}")
    print(f"Country: {location['country']}")

    print("\nCurrent Weather:")

    print(
        f"Temperature: {current['temperature_2m']}"
        f"{units['temperature_2m']}"
    )

    print(
        f"Feels Like: {current['apparent_temperature']}"
        f"{units['apparent_temperature']}"
    )

    print(
        f"Condition: {description}"
    )

    print(
        f"Humidity: {current['relative_humidity_2m']}"
        f"{units['relative_humidity_2m']}"
    )

    print(
        f"Wind Speed: {current['wind_speed_10m']}"
        f"{units['wind_speed_10m']}"
    )

    print(
        f"Precipitation: {current['precipitation']}"
        f"{units['precipitation']}"
    )

    print(
        f"Daytime: {'Yes' if current['is_day'] else 'No'}"
    )

    print(f"Last Updated: {current['time']}")

    print("================================")


# Main application
def main():

    print("\n================================")
    print("       WEATHER APPLICATION")
    print("================================")

    while True:

        city = input(
            "\nEnter city name (or type 'exit'): "
        ).strip()

        if city.lower() == "exit":
            print("Thank you for using Weather Application!")
            break

        if not city:
            print("Please enter a valid city name!")
            continue

        try:

            print("\nFetching weather information...")

            location = get_city_coordinates(city)

            if location is None:
                print("City not found! Try another city.")
                continue

            weather = get_weather(
                location["latitude"],
                location["longitude"]
            )

            display_weather(location, weather)

        except requests.exceptions.Timeout:
            print("Request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            print("Network error. Check your internet connection.")

        except requests.exceptions.HTTPError:
            print("Weather service returned an error.")

        except requests.exceptions.RequestException as error:
            print("An error occurred:", error)

        except (KeyError, IndexError, TypeError, ValueError):
            print("Unable to process weather data.")


if __name__ == "__main__":
    main()
