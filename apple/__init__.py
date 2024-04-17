import requests
from geopy.distance import geodesic

class AppleMaps():
    def __init__(self, apple_maps_key: str):
        self.apple_maps_key = apple_maps_key

    def _bounding_box(self, latitude, longitude, distance_km=2) -> str:
        center_point = (latitude, longitude)

        north = geodesic(kilometers=distance_km).destination(center_point, 0).latitude
        south = geodesic(kilometers=distance_km).destination(center_point, 180).latitude
        east = geodesic(kilometers=distance_km).destination(center_point, 90).longitude
        west = geodesic(kilometers=distance_km).destination(center_point, 270).longitude

        return f"{north},{east},{south},{west}"


    def _get_access_token(self, map_token) -> str:
        url = f"https://maps-api.apple.com/v1/token"
        headers = {"accept": "application/json", "Authorization": f"Bearer {map_token}"}

        response = requests.get(url, headers=headers)
        response = response.json()
        return response["accessToken"]


    def apple_get_places(self, latitude: str, longitude: str, category: str, poi: str) -> str:
        search_region = self._bounding_box(latitude, longitude)
        url = f"https://maps-api.apple.com/v1/search?q={category}&searchRegion={search_region}&includePoiCategories={poi}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self._get_access_token(self.apple_maps_key)}",
        }

        response = requests.get(url, headers=headers)
        response = response.json()
        
        print(response)