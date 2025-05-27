import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Grouper

data = pd.read_csv('Cochin_ENC_2016_hourly.csv', header = 0, index_col = 0, parse_dates = True)

# plt.title('Tide Data')
# plt.xlabel('Date & Time')
# plt.xlabel('Water Level (m)')

groups = data.groupby(Grouper(freq = 'A'))

years = pd.DataFrame()
for name, group in groups:
	years[name.year] = group.values
years.plot(subplots=True, legend=False)


#data.plot(title = 'Tide Data', xlabel = 'Date & Time', ylabel = 'Water Level (m)')
plt.show()




