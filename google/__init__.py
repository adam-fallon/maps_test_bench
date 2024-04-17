import googlemaps
import os

class GoogleMaps:
    def __init__(self, google_maps_key: str):
        self.google_maps_key = google_maps_key

    def geocode(self, location_name: str):
        gmaps = googlemaps.Client(key=f"{self.google_maps_key}")
        geocode_result = gmaps.geocode(location_name)
        return geocode_result

    def google_nearby_places(self, location_name: str):
        GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

        gmaps = googlemaps.Client(key=f"{GOOGLE_MAPS_KEY}")
        lat_long = self.geocode(location_name)

        places = gmaps.places_nearby(
            location=lat_long[0]["geometry"]["location"],
            radius=1000,
            open_now=True,
            type="restaurant",
        )

        print(places)