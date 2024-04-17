import googlemaps
from datetime import datetime
import os

from dotenv import load_dotenv

load_dotenv()
GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

gmaps = googlemaps.Client(key=f"{GOOGLE_MAPS_KEY}")

lat_long = gmaps.geocode("1600 Amphitheatre Parkway, Mountain View, CA")

now = datetime.now()

places = gmaps.places_nearby(
    location=lat_long[0]["geometry"]["location"],
    radius=1000,
    open_now=True,
    type="restaurant",
)

print(places)