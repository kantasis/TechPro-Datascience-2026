import json
import numpy as np

filename_str = 'forecast.json'
with open(filename_str,'r') as f:
   data_str = f.read()


data_dict = json.loads(data_str)

time_list = data_dict['hourly']['time']
temp_list = data_dict['hourly']['temperature_2m']

matrix = []

matrix_np = np.array([time_list, temp_list])
matrix_np = matrix_np.T

print(matrix_np)

# np.savetxt('forecast.csv', matrix_np,fmt='%s')













