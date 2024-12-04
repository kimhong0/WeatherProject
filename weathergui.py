import tkinter as tk
from tkinter import ttk
from weather import get_weather_data  # Import the logic from weather_api.py

# Function to handle weather fetching and UI updates
def fetch_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="City name cannot be empty!", fg="red")
        return

    weather_data = get_weather_data(city)

    if "error" in weather_data:
        result_label.config(text=weather_data["error"], fg="red")
    else:
        # Update UI with fetched weather data
        city_label.config(text=weather_data["city"])
        time_label.config(text=weather_data["time"])
        temp_label.config(text=weather_data["temperature"])
        feels_label.config(text=weather_data["feels_like"])
        desc_label.config(text=weather_data["description"])
        wind_value_label.config(text=weather_data["wind_speed"])
        humidity_value_label.config(text=weather_data["humidity"])
        pressure_value_label.config(text=weather_data["pressure"])
        result_label.config(text="Weather data updated!", fg="green")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x400")
root.configure(bg="#E6F7FF")

# Top Frame (City Search and Time)
top_frame = tk.Frame(root, bg="#E6F7FF")
top_frame.pack(pady=10, padx=20, fill="x")

city_label = tk.Label(top_frame, text="Enter city:", font=("Arial", 14), bg="#E6F7FF")
city_label.grid(row=0, column=0, padx=5)

city_entry = ttk.Entry(top_frame, font=("Arial", 14), width=20)
city_entry.grid(row=0, column=1, padx=5)

search_button = ttk.Button(top_frame, text="Search", command=fetch_weather)
search_button.grid(row=0, column=2, padx=5)

time_label = tk.Label(top_frame, text="", font=("Arial", 14), bg="#E6F7FF")
time_label.grid(row=0, column=3, padx=20)

# Middle Frame (Main Weather Info)
middle_frame = tk.Frame(root, bg="#FFFFFF", relief="raised", bd=2)
middle_frame.pack(pady=10, padx=20, fill="x")

city_label = tk.Label(middle_frame, text="", font=("Arial", 20, "bold"), bg="#FFFFFF")
city_label.pack()

temp_label = tk.Label(middle_frame, text="", font=("Arial", 50, "bold"), bg="#FFFFFF", fg="#FF5733")
temp_label.pack()

feels_label = tk.Label(middle_frame, text="", font=("Arial", 14), bg="#FFFFFF")
feels_label.pack()

desc_label = tk.Label(middle_frame, text="", font=("Arial", 16), bg="#FFFFFF", fg="#555555")
desc_label.pack(pady=10)

# Bottom Frame (Weather Details)
bottom_frame = tk.Frame(root, bg="#87CEEB")
bottom_frame.pack(pady=10, padx=20, fill="x")

# Weather detail labels and values
wind_label = tk.Label(bottom_frame, text="Wind: ", font=("Arial", 14), bg="#87CEEB")
wind_label.grid(row=0, column=0, padx=10, pady=5)

wind_value_label = tk.Label(bottom_frame, text="", font=("Arial", 14), bg="#87CEEB")
wind_value_label.grid(row=1, column=0, padx=10, pady=5)

humidity_label = tk.Label(bottom_frame, text="Humidity: ", font=("Arial", 14), bg="#87CEEB")
humidity_label.grid(row=0, column=1, padx=10, pady=5)

humidity_value_label = tk.Label(bottom_frame, text="", font=("Arial", 14), bg="#87CEEB")
humidity_value_label.grid(row=1, column=1, padx=10, pady=5)

pressure_label = tk.Label(bottom_frame, text="Pressure: ", font=("Arial", 14), bg="#87CEEB")
pressure_label.grid(row=0, column=2, padx=10, pady=5)

pressure_value_label = tk.Label(bottom_frame, text="", font=("Arial", 14), bg="#87CEEB")
pressure_value_label.grid(row=1, column=2, padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#E6F7FF", fg="red")
result_label.pack()

# Run the app
root.mainloop()
