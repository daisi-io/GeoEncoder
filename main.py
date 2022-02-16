from geopy.geocoders import Nominatim


def address_to_coordinates(address):
    # Geopy has different Geocoding services that you can choose from, including Google Maps, ArcGIS, AzureMaps, Bing, etc. Some of them require API keys, while others do not need.
    # Complete list of encoder: https://geopy.readthedocs.io/en/latest/#module-geopy.geocoders
    # Nominatim Geocoding service, which is built on top of OpenStreetMap data
    
    geolocator = Nominatim(user_agent="daisi_geocoder")

    location = geolocator.geocode(address)

    data = {
        "address": location.address if location else None,
        "latitude": location.latitude if location else None,
        "longitude": location.longitude if location else None,
    }

    return [{"id": "address_to_coordinates", "type": "json", "data": data}]


def coordinates_to_address(latitude, longitude):
    geolocator = Nominatim(user_agent="daisi_geocoder")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    
    data = {
        "address": location.address if location else None,
        "latitude": location.latitude if location else None,
        "longitude": location.longitude if location else None,
    }
    
    return [{"id": "coordinates_to_address", "type": "json", "data": data}]
    
if __name__ == "__main__": 
    # print(parse_address("8803 Willow Wind Ln Houston"))
    print(address_to_coordinates("Champ de Mars, Paris, France"))
    print(coordinates_to_address(52.509669, 13.376294))