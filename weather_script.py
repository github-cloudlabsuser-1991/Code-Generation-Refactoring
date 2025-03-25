import requests

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(f"Clima en {city}: {data['weather'][0]['description']}")

if __name__ == "__main__":
    # ...puedes reemplazar estos valores por tus datos...
    api_key = "<TU_API_KEY>"
    city = "Madrid"
    get_weather(api_key, city)
