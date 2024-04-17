import os
from dotenv import load_dotenv
from google import GoogleMaps
from apple import AppleMaps

load_dotenv()
GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
APPLE_MAPS_API_KEY = os.getenv("APPLE_MAPS_API_KEY")

google = GoogleMaps(GOOGLE_MAPS_KEY)
apple = AppleMaps(APPLE_MAPS_API_KEY)


if __name__ == "__main__":
    # https://developer.apple.com/documentation/applemapsserverapi/
    apple.apple_get_places("37.7749", "-122.4194", "restaurant", "FoodMarket")
    # https://developers.google.com/maps/documentation
    google.google_nearby_places("London Paddington")