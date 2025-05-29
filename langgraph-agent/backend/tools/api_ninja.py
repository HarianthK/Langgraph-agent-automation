# import os
# import requests
# from dotenv import load_dotenv  # type: ignore

# load_dotenv()  # Loading .env file

# API_NINJA_KEY = os.getenv("API_NINJA_KEY")

# BASE_URL = "https://api.api-ninjas.com/v1"


# def get_location_from_zip(zip_code: str):
#     response = requests.get(f"{BASE_URL}/zipcode?zip={zip_code}", headers={
#         "X-Api-Key": API_NINJA_KEY
#     })
#     if response.status_code == 200:
#         return response.json()
#     print("❌ Failed to get ZIP code info:", response.text)
#     return []


# def get_city_demographics(city: str, state: str):
#     response = requests.get(f"{BASE_URL}/city?name={city}&state={state}", headers={
#         "X-Api-Key": API_NINJA_KEY
#     })
#     if response.status_code == 200:
#         return response.json()
#     print("❌ Failed to get demographics:", response.text)
#     return []


# def get_location_from_full_address(street: str, city: str, state: str):
#     address = f"{street}, {city}, {state}"
#     response = requests.get(f"{BASE_URL}/geocoding?address={address}", headers={
#         "X-Api-Key": API_NINJA_KEY
#     })
#     if response.status_code == 200:
#         return response.json()
#     print("❌ Failed to geocode full address:", response.text)
#     return []

import os
import requests
from dotenv import load_dotenv  # type: ignore

load_dotenv()

API_NINJA_KEY = os.getenv("API_NINJA_KEY")
BASE_URL = "https://api.api-ninjas.com/v1"


def get_zip_info(city: str, state: str):
    response = requests.get(f"{BASE_URL}/zipcode?city={city}&state={state}", headers={
        "X-Api-Key": API_NINJA_KEY
    })
    if response.status_code == 200:
        return response.json()
    print("❌ Failed to get ZIP info:", response.text)
    return []


def get_city_demographics(city: str, state: str):
    response = requests.get(f"{BASE_URL}/city?name={city}&state={state}", headers={
        "X-Api-Key": API_NINJA_KEY
    })
    if response.status_code == 200:
        return response.json()
    print("❌ Failed to get demographics:", response.text)
    return []
