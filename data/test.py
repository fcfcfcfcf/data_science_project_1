import numpy as np
import pandas as pd
import csv

data_frame_weather = None
with open('./data/weather_data.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    headers = []
    data = []
    for row in f:
        if not line_count:
            headers = [x.replace('"', '') for x in row.rstrip().split(',')]
        else:
            data.append([row.rstrip().split(',')[0].replace('"', '')] + [bool(x) for x in row.rstrip().split(',')[1:]])
        line_count += 1
    data_frame_weather = pd.DataFrame(data=data, columns=headers)
            
            
print(len(data))