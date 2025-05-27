# from pathlib import Path

# import numpy as np
# import pandas as pd

# %matplotlib inline

# import matplotlib.pyplot as plt
# import seaborn as sns

# plt.rcParams['figure.figsize'] = (8, 4)
# plt.rcParams['figure.max_open_warning'] = 1250

# DATA_PATH = Path('../input/ashrae-energy-prediction')

# train_df = pd.read_csv(DATA_PATH/'train.csv',parse_dataes = ['timestamp'])
# test_df = pd.read_csv(DATA_PATH/'test.csv', parse_dates = ['timestamp'])
# building_df = pd.read_csv(DATA_PATH/'building_metadata.csv')

# train_df.groupby('timestamp')['meter'].count().plot()

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[1])
print(arr[2] + arr[3])


