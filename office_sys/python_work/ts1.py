import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load time series data into a Pandas DataFrame
data = pd.read_csv('daily-min-temperatures.csv', index_col=1, parse_dates=True)

# Plot the time series data
plt.plot(data)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('WaterLevel')
plt.show()

# Resample the time series data to a lower frequency
weekly_data = data.resample('W').mean()
hourly_data = data.resample('H').mean()

# Plot the resampled data
plt.plot(weekly_data)
plt.title('Weekly Resampled Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Perform a rolling average on the time series data
rolling_data = data.rolling(window=30).mean()

# Plot the rolling average data
plt.plot(rolling_data)
plt.title('Rolling Average Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

# Perform a time series decomposition on the data
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(data)

# Plot the decomposition
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(data, label='Original')
plt.legend(loc='upper left')

plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='upper left')

plt.subplot(413)
plt.plot(seasonal,label='Seasonality')
plt.legend(loc='upper left')

plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()