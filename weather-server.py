from mcp.server.fastmcp import FastMCP
import os
import requests
from dotenv import load_dotenv
import traceback

load_dotenv()
mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get real-time weather for a city (temp & humidity in Celsius)."""
    try:
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            print("ERROR: WEATHER_API_KEY not found in env.")
            return "ERROR: WEATHER_API_KEY missing."

        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        print(f"Calling URL: {url}")

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        condition = data["current"]["condition"]["text"]

        result = f"{city}: {condition}, Temp: {temp}°C, Humidity: {humidity}%"
        print("Returning result:", result)
        return result

    except Exception as e:
        print("Weather tool error:\n", traceback.format_exc())
        return f"ERROR: Weather data could not be fetched: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
