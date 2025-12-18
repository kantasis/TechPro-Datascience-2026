import json
import numpy as np
import requests 


url = 'https://api.open-meteo.com/v1/forecast'
params = {
   "latitude": 40.6436,
   "longitude": 22.9309,
   "hourly": "temperature_2m",
   "start_date": "2025-12-19",
   "end_date": "2025-12-19"
}

response = requests.get(url, params = params)

if response.status_code != 200:
   print(f"An error occurred {response.status_code}")
   exit()

data_str = response.text
data_dict = json.loads(data_str)

times_list = data_dict['hourly']['time']
temperatures_list = data_dict['hourly']['temperature_2m']

matrix_np = np.array([times_list, temperatures_list])
matrix_np = matrix_np.T

np.savetxt('forecast.csv', matrix_np, delimiter=',', fmt='%s') 
print(matrix_np)


 











