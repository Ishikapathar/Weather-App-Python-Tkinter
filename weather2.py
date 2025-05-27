import requests
import tkinter as tk
from tkinter import messagebox

# --- API Setup ---
API_KEY = "31d151b01fce393f22f05f7bf6337d50"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# --- Fetch Weather Function ---
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city.strip(),
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        print(data)  # Debug print

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"].title()

            result = f"📍 City: {city.title()}\n🌡️ Temperature: {temp}°C\n💧 Humidity: {humidity}%\n🌤️ Condition: {condition}"
            
            output_box.config(state="normal")  # Enable editing
            output_box.delete(1.0, tk.END)  # Clear previous output
            output_box.insert(tk.END, result)  # Insert new output
            output_box.config(state="disabled")  # Make it read-only again
        else:
            messagebox.showerror("Error", f"{data.get('message', 'City not found')}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# --- UI Setup ---
root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("400x320")
root.configure(bg="#f0f0f0")

# Heading
heading = tk.Label(root, text="Weather App", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
heading.pack(pady=10)

# City Entry
city_entry = tk.Entry(root, font=("Helvetica", 14), width=25)
city_entry.pack(pady=10)

# Get Weather Button
get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12), bg="#4caf50", fg="white")
get_button.pack(pady=5)

# Output Box
output_box = tk.Text(root, height=5, width=40, font=("Helvetica", 12), bg="#ffffff", state="disabled", wrap="word")
output_box.pack(pady=20)

# Run the app
root.mainloop()
