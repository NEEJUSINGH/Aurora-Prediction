import requests
from bs4 import BeautifulSoup
import sqlite3

def check_aurora():
    # city and api_key 
    url = "http://api.openweathermap.org/data/2.5/weather?q={Minneapolis}&appid={c8aee7a2475d74d22638d3080c2b681e}"
    response = requests.get(url)
    data = response.json()

    # Check if the API response contains the expected structure
    if "weather" in data and data["weather"]:
        for weather_info in data["weather"]:
            if "aurora" in weather_info["description"].lower():
                return True
    
    return False
    

def insert_data(data):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    for item in data:
        c.execute("INSERT INTO data (name, value) VALUES (?, ?)", (item['name'], item['value']))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    if check_aurora():
        print("Aurora is happening nearby!")
    else:
        print("No aurora forecast nearby.")
