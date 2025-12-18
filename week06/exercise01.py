import requests
import numpy as np

url = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 40.6436,
"longitude": 22.9309,
"hourly": "temperature_2m",
"start_date": "2025-12-19",
"end_date": "2025-12-19"
}

response = requests.get(url, params=params)
print(response.status_code)
#print(response.text)

data_str = response.text
print(data_str)
data_dict = json.loads(data_str)
#print(data_dict)
#type(data_dict)

matrix_np = []


for i in range(len(data_dict['hourly']['temperature_2m'])):
  matrix_np.append((data_dict['hourly']['time'][i],data_dict['hourly']['temperature_2m'][i]))

a = np.asarray(matrix_np)
np.savetxt("tomorrowforecast.csv", a, delimiter=",",fmt="%s")