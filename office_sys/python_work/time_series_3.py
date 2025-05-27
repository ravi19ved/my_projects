# from pandas import read_csv
# from pandas import DataFrame
# from pandas import Grouper
# from matplotlib import pyplot


# series = read_csv('daily-min-temperatures.csv', header=0,
#                   index_col=0, parse_dates=True, squeeze=True)
# groups = series.groupby(Grouper(freq='A'))
# years = DataFrame()

# for name, group in groups:
# 	years[name.year] = group.values
# years.plot(subplots=True, legend=False)
# pyplot.show()


from pandas import read_csv
from matplotlib import pyplot
series = read_csv('daily-min-temperatures.csv', header=0,
                  index_col=0, parse_dates=True, squeeze=True)
series.plot(style = 'k.')
pyplot.show()
