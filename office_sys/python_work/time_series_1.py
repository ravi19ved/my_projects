import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
help(df.cumsum)
df = df.cumsum()

df = pd.concat([df['Jan 2000':'Aug 2000'], df['Jan 2001':'Aug 2001']])
df.plot()

plt.show()