from dataclasses import dataclass
import requests
import argparse

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str)
args = parser.parse_args()

if args.city:
    url += f"&by_city={args.city}"


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float
    latitude: float
    phone: str
    website_url: str
    state: str
    street: str

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country}"


response = requests.get(url)
data = response.json()
lista = [Brewery(**brewery) for brewery in data]

for i in lista:
    print(i)
