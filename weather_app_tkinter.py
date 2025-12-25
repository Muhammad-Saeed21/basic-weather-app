import tkinter as tk
from tkinter import ttk, messagebox
import requests

# ---------------------------
# API Configuration
# ---------------------------
API_KEY = "934723f945c12613ad65d16e5927c826"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Pakistan Cities List
PAKISTAN_CITIES = [
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad",
    "Multan", "Peshawar", "Quetta", "Sialkot", "Gujranwala",
    "Hyderabad", "Bahawalpur", "Sukkur"
]

# ---------------------------
# Fetch Weather Function
# ---------------------------
def get_weather():
    city = city_var.get()

    # FIX 1: Proper city validation
    if city == "" or city == "Select City":
        messagebox.showwarning("Warning", "Please select a city")
        return

    params = {
        "q": f"{city},PK",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # FIX 2: cod ko string/int dono handle karo
        if str(data.get("cod")) != "200":
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_label.config(
    text=(
        f"📍  City: {city}\n\n"
        f"🌡  Temperature :  {temp} °C\n"
        f"🌤  Condition   :  {weather}\n"
        f"💧  Humidity    :  {humidity}%\n"
        f"💨  Wind Speed  :  {wind} m/s"
    )
)


    except Exception as e:
        messagebox.showerror("Error", "Network or API error")

# ---------------------------
# Tkinter UI
# ---------------------------
root = tk.Tk()
root.title("Pakistan Weather App")
root.geometry("420x420")
root.minsize(380, 380)
root.configure(bg="#1e272e")

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 11), padding=8)

# Heading
heading = tk.Label(
    root,
    text="🌦 Pakistan Weather Checker",
    font=("Segoe UI", 16, "bold"),
    fg="white",
    bg="#1e272e"
)
heading.pack(pady=15)

# City Selection
city_var = tk.StringVar()
city_dropdown = ttk.Combobox(
    root,
    textvariable=city_var,
    values=PAKISTAN_CITIES,
    font=("Segoe UI", 11),
    state="readonly"
)
city_dropdown.pack(pady=10)
city_dropdown.set("Select City")

# Button
check_btn = ttk.Button(
    root,
    text="Check Weather",
    command=get_weather
)
check_btn.pack(pady=10)

# Result Box
result_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 11),
    fg="white",
    bg="#485460",
    justify="left",
    width=40,
    height=10
)
result_label.pack(pady=15)

# Footer
footer = tk.Label(
    root,
    text="Developed by Muhammad Saeed",
    font=("Segoe UI", 9),
    fg="#d2dae2",
    bg="#1e272e"
)
footer.pack(side="bottom", pady=8)

root.mainloop()