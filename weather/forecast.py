def process_weather_data(data):
    if data:
        forecast_days = data['forecast']['forecastday']
        processed_data = []
        for day in forecast_days:
            date = day['date']
            day_data = day['day']
            processed_data.append({
                'date': date,
                'temperature': day_data['avgtemp_c'],
                'max_temp': day_data['maxtemp_c'],
                'min_temp': day_data['mintemp_c'],
                'humidity': day_data['avghumidity'],
                'condition': day_data['condition']['text']
            })
        return processed_data
    else:
        return None
