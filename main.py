import tkinter as tk
from tkinter import messagebox
from weather.api import get_weather
from weather.forecast import process_weather_data
from weather.plot import plot_weather
import json
import os
import logging
import sqlite3
import unicodedata
import re

# Loglama yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')

def save_weather_data(data, city):
    filename = f"{city}_weather.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.info(f"Weather data saved for {city} in {filename}")

def normalize_city_name(city_name):
    normalized_name = unicodedata.normalize('NFKD', city_name).encode('ASCII', 'ignore').decode('utf-8')
    normalized_name = re.sub(r'[^a-zA-Z0-9]', '', normalized_name.lower())
    return normalized_name

def save_to_db(city, weather_data):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()

    table_name = normalize_city_name(city)

    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            max_temp REAL,
            min_temp REAL,
            avg_temp REAL,
            condition TEXT,
            humidity REAL,
            latitude REAL,
            longitude REAL,
            wind_speed REAL,
            last_updated TEXT,
            current_temp REAL,
            current_condition TEXT,
            current_humidity REAL
        )
    ''')

    for day in weather_data:
        c.execute(f'''
            INSERT INTO {table_name} (date, max_temp, min_temp, avg_temp, condition, humidity, latitude, longitude, wind_speed, last_updated, current_temp, current_condition, current_humidity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            day['date'], day['max_temp'], day['min_temp'], day['temperature'], day['condition'],
            day['humidity'], day['latitude'], day['longitude'], day['wind_speed'],
            day['last_updated'], day['current_temp'], day['current_condition'], day['current_humidity']
        ))

    conn.commit()
    conn.close()
    logging.info(f"Weather data saved for {city} to the database")

def show_weather():
    city = city_entry.get()
    logging.info(f"Fetching weather data for {city}")
    data = get_weather(city)
    if data:
        weather = process_weather_data(data)
        if weather:
            save_weather_data(data, city)
            save_to_db(city, weather)
            plot_weather(weather)
            logging.info(f"Weather data processed and plotted for {city}")
            messagebox.showinfo("Hava Durumu", "Veriler başarıyla kaydedildi ve tablo gösterildi.")
        else:
            logging.error("Error processing weather data")
            messagebox.showerror("Hata", "Veriler işlenirken bir hata oluştu.")
    else:
        logging.error("Error fetching weather data")
        messagebox.showerror("Hata", "Hava durumu verileri alınamadı.")

# GUI kurulum
root = tk.Tk()
root.title("Hava Durumu Uygulaması")

city_label = tk.Label(root, text="Şehir ismini girin:")
city_label.pack()

city_entry = tk.Entry(root, width=100)
city_entry.pack()

get_weather_button = tk.Button(root, text="Hava Durumunu Göster", command=show_weather)
get_weather_button.pack()

root.mainloop()
