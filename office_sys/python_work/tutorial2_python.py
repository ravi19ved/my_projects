import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

#Variable Declarations:
cost_of_ice_bag = 1.25
profit_margin = 0.2
number_of_bags = 400

profit_per_bag = cost_of_ice_bag * profit_margin
total_profit = profit_per_bag * number_of_bags
print(total_profit)

my_string = "Hello World"

num_years = 4
days_per_year = 365.25
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

#Calculate number of seconds in four years

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
print(hours_per_day)

