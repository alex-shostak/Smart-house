import os

for file in os.listdir('sensor_data'):
    os.remove('sensor_data/' + file)
