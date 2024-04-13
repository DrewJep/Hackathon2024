from flask import *
import requests
import json
from pathlib import Path


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mtn_response=query_resort_all().json()
    print(mtn_response)
    return render_template("index.html", mtn_data=mtn_response)

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    return render_template("detail.html")

@app.route('/prepare', methods=['GET', 'POST'])
def prepare():
    mtn_data=request.form('search')
    query(mountian=mtn_data)
    return render_template('detail.html',mtn=mtn_data)


#### API Stuff ####
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

def query(mountian):
    if mountian==None:
        response = query_resort_all()
        write_to_file(response.json(),'all')
    else:
        response = query_resort(mountian)
        write_to_file(response.json(),f'{mountian}')

        response = query_weather(response.json()["data"]["location"]['latitude'],response.json()["data"]["location"]['longitude'])
        write_to_file(response.json(),f'{mountian}-weather')

if __name__ == '__main__':
    app.run(debug=True)