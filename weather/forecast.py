def process_weather_data(data):
    if data:
        location = data['location']
        current = data['current']
        forecast_days = data['forecast']['forecastday']
        processed_data = [{
            'date': 'Anlık Durum',
            'max_temp': current['temp_c'],  # Anlık sıcaklık, max_temp olarak
            'min_temp': current['temp_c'],  # Anlık sıcaklık, min_temp olarak
            'temperature': current['temp_c'],  # Anlık sıcaklık, ortalama sıcaklık olarak
            'condition': current['condition']['text'],
            'humidity': current['humidity'],
            'latitude': location['lat'],
            'longitude': location['lon'],
            'wind_speed': current['wind_kph'],
            'last_updated': current['last_updated'],
            'current_temp': current['temp_c'],  # Anlık sıcaklık, current_temp olarak
            'current_condition': current['condition']['text'],
            'current_humidity': current['humidity']
        }]
        for day in forecast_days:
            date = day['date']
            day_data = day['day']
            processed_data.append({
                'date': date,
                'max_temp': day_data['maxtemp_c'],
                'min_temp': day_data['mintemp_c'],
                'temperature': day_data['avgtemp_c'],
                'condition': day_data['condition']['text'],
                'humidity': day_data['avghumidity'],
                'latitude': location['lat'],
                'longitude': location['lon'],
                'wind_speed': day_data['maxwind_kph'],
                'last_updated': current['last_updated'],
                'current_temp': current['temp_c'],
                'current_condition': current['condition']['text'],
                'current_humidity': current['humidity']
            })
        return processed_data
    else:
        return None
