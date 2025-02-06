def process_weather_data(data):
    if data:
        location = data['location']
        forecast_days = data['forecast']['forecastday']
        processed_data = []
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
                'last_updated': data['current']['last_updated']
            })
        return processed_data
    else:
        return None
