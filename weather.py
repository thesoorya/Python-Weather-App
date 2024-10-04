import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv() 

async def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception("City not found or API request failed.")

def display_weather(data):
    city = data['name']
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    print(f"Weather in {city}: {temperature}°C, {weather}, Humidity: {humidity}%")

async def main():
    while True:
        city = input("Enter a city name (or type 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        try:
            weather_data = await fetch_weather(city) ##used to fetch data from api 
            display_weather(weather_data) ##displaying the data from api
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())