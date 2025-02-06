import tkinter as tk
from tkinter import messagebox
from weather.api import get_weather
from weather.forecast import process_weather_data
from weather.plot import plot_weather
import json
import os

def save_weather_data(data, city):
    # Kayıt için dosya adı
    filename = f"{city}_weather.json"
    # Veriyi JSON formatında kaydet
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def show_weather():
    city = city_entry.get()
    data = get_weather(city)
    if data:
        weather = process_weather_data(data)
        if weather:
            save_weather_data(data, city)
            plot_weather(weather)
            messagebox.showinfo("Hava Durumu", "Veriler başarıyla kaydedildi ve grafik gösterildi.")
        else:
            messagebox.showerror("Hata", "Veriler işlenirken bir hata oluştu.")
    else:
        messagebox.showerror("Hata", "Hava durumu verileri alınamadı.")

# GUI kurulum
root = tk.Tk()
root.title("Hava Durumu Uygulaması")

city_label = tk.Label(root, text="Şehir ismini girin:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Hava Durumunu Göster", command=show_weather)
get_weather_button.pack()

root.mainloop()
