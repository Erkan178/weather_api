import matplotlib.pyplot as plt
import logging

# Loglama yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')

def plot_weather(weather_data):
    # Verileri tabloya dönüştür
    dates = [day['date'] for day in weather_data]
    max_temps = [day['max_temp'] for day in weather_data]
    min_temps = [day['min_temp'] for day in weather_data]
    avg_temps = [day['temperature'] for day in weather_data]
    conditions = [day['condition'] for day in weather_data]
    humidities = [day['humidity'] for day in weather_data]
    latitudes = [day['latitude'] for day in weather_data]
    longitudes = [day['longitude'] for day in weather_data]
    wind_speeds = [day['wind_speed'] for day in weather_data]
    last_updates = [day['last_updated'] for day in weather_data]

    # Tablo verileri
    table_data = [
        ["Date", "Max Temp", "Min Temp", "Avg Temp", "Condition", "Humidity", "Latitude", "Longitude", "Wind Speed", "Last Update"],
        *zip(dates, max_temps, min_temps, avg_temps, conditions, humidities, latitudes, longitudes, wind_speeds, last_updates)
    ]

    # Tabloyu oluştur
    fig, ax = plt.subplots(figsize=(16, 8))  # Daha büyük bir figür boyutu ayarlayın
    ax.axis('tight')
    ax.axis('off')

    # Tabloyu ekleyin
    table = ax.table(cellText=table_data, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)  # Yazı boyutunu ayarlayın
    table.scale(1.2, 1.2)  # Tabloyu ölçeklendirin

    # Başlık ekle
    plt.title('3 Günlük Hava Durumu Verileri ve Anlık Durum', fontsize=14)

    # Tabloyu göster
    plt.show()
    logging.info("Weather data table plotted")
