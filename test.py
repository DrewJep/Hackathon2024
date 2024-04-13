import requests
import json

def write_to_file(response,name):
    file_path = f"data/{name}.json"
    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the JSON data to the file
        json.dump(response, file, indent=4)

def query_resort(mountain):
    url = f"https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort/{mountain}"

    headers = {
        "X-RapidAPI-Key": "6eeb8d061dmsh2aaa343775263eep1e5f01jsn5ff8f6bd7688",
        "X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response

def query_resort_all():
    url = "https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort"

    headers = {
        "X-RapidAPI-Key": "6eeb8d061dmsh2aaa343775263eep1e5f01jsn5ff8f6bd7688",
        "X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response


def query_weather(lat, long):
    url = f'https://api.weather.gov/points/{lat},{long}'
    response = requests.get(url)
    office=response.json()['properties']['gridId']
    gridX=response.json()['properties']['gridX']
    gridY=response.json()['properties']['gridY']

    url = f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast'
    response = requests.get(url)
    return response

############################## MAIN ##############################
def query(mountian):
    if mountian==None:
        response = query_resort_all()
        write_to_file(response.json(),'all')
    else:
        response = query_resort(mountian)
        write_to_file(response.json(),f'{mountian}')

        response = query_weather(response.json()["data"]["location"]['latitude'],response.json()["data"]["location"]['longitude'])
        write_to_file(response.json(),f'{mountian}-weather')

query(None)

with open('data/all.json', "r") as file:
    # Load the JSON data from the file
    data = json.load(file)
    print(data.json())
    # temp = "49 Degrees North"
    # for i in data:
    #     if data['name']==temp:
    #         print("hi")