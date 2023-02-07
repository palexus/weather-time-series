import requests
import datetime



url = "https://dwd.api.proxy.bund.dev/v30/stationOverviewExtended?stationIds=03313"


response = requests.get(url)
data = response.json()["03313"] # Berlin Tegel Klimadaten


data["forecast1"].keys()
temperature = data["forecast1"]["temperature"]
start = data["forecast1"]["start"]
data["forecast1"]["timeStep"]
len(data["forecast1"]["temperatureStd"])
len(temperature)

datetime.datetime.fromtimestamp(start/1000)
datetime.datetime.fromtimestamp(-10000000)


