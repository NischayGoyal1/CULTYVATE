import requests

def nisch(location):
    data=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=bae363c55a4f3c7563608369a789e456")
    data=data.json()


    nis={
        "tempmin":data["main"]["temp_min"],
        "tempmax":data["main"]["temp_max"],
        "pres":data["main"]["pressure"],
        "humidity":data["main"]["humidity"]
    }
    return nis








