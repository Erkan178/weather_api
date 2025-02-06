def save_weather_data(data, city):
    # Kayıt için dosya adı
    filename = f"{city}_weather.json"
    # Veriyi JSON formatında kaydet
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
