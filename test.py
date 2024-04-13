import requests
import json

def write_to_file(response):
    file_path = "data.json"
        
    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the JSON data to the file
        json.dump(response, file, indent=4)

# def query_resort(mountain):
#     url = f"https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort/{mountain}"

#     headers = {
#         "X-RapidAPI-Key": "6eeb8d061dmsh2aaa343775263eep1e5f01jsn5ff8f6bd7688",
#         "X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers)
#     return response

# response = query_resort('whistler-blackcomb')
# write_to_file(response.json())

# print(response.json()["data"]["location"]['latitude'])

url = "https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort"

headers = {
	"X-RapidAPI-Key": "6eeb8d061dmsh2aaa343775263eep1e5f01jsn5ff8f6bd7688",
	"X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

write_to_file(response.json())


# def query_weather(long, lat):
#     url = https://api.weather.gov/points/39.7456,-97.0892
#     response = requests.get(url)
#     print()