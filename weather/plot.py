import matplotlib.pyplot as plt
import logging

# Loglama yapılandırması
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')

def plot_weather(data):
    dates = [d['date'] for d in data]
    temperatures = [d['temperature'] for d in data]
    max_temps = [d['max_temp'] for d in data]
    min_temps = [d['min_temp'] for d in data]
    humidities = [d['humidity'] for d in data]
    conditions = [d['condition'] for d in data]

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Tarih')
    ax1.set_ylabel('Sıcaklık (°C)', color='tab:red')
    ax1.plot(dates, temperatures, 'r-', label='Ortalama Sıcaklık')
    ax1.plot(dates, max_temps, 'r--', label='Maksimum Sıcaklık')
    ax1.plot(dates, min_temps, 'r:', label='Minimum Sıcaklık')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Nem (%)', color='tab:blue')
    ax2.plot(dates, humidities, 'b-', label='Nem')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    for i, txt in enumerate(conditions):
        ax1.annotate(txt, (dates[i], temperatures[i]), textcoords="offset points", xytext=(0,10), ha='center')

    fig.tight_layout()
    plt.title('3 Günlük Hava Tahmini')
    fig.legend(loc='upper right')
    plt.show()
