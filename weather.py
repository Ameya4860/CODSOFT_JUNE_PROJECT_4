import tkinter as tk
import json
import urllib.request

# Replace with your Weather API URL and API key
API_KEY = "716a1cb0d8714a7196772300230409"
WEATHER_API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q="

def fetch_weather(city):
    try:
        # Create the API URL
        api_url = WEATHER_API_URL + city
        # Fetch data from the API
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode('utf-8'))
            temperature = data.get("current", {}).get("temp_c", "N/A")
            return f"Temperature in {city}: {temperature}°C"
    except Exception as e:
        return f"Error fetching data: {str(e)}"

def get_weather():
    city = city_entry.get()
    result_label.config(text=fetch_weather(city))

# Create the main application window
app = tk.Tk()
app.title("Weather App")

# Create and configure GUI elements
city_label = tk.Label(app, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(app, text="", wraplength=300)
result_label.pack()

# Start the GUI application
app.mainloop()
