import requests
from bs4 import BeautifulSoup
response = requests.get("https://media-downloader-7ovf.onrender.com/api/ping")
print(response)

data = response.json()
print(data)

page = requests.get("https://media-saver-hub.vercel.app")
soup = BeautifulSoup(page.text, "html.parser")
print(soup)





# Ternary Operator
name = "Incognito"
age = 119
print(f"Welcome, {name}") if age >= 18 else print("Access Denied")