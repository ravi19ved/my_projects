from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'D:\INCOIS\Tide\INCOIS_INSAT\Chennai\Chennai_All_Data\Chennai_ENC_2011.csv'

data = pd.read_csv(file_path)
df = pd.DataFrame(data, columns = ['Serial','DateTime', 'TideLevel' ])


#Setting the Date as Index

df['DateTime'] = pd.to_datetime(df['DateTime'])
df.index = df['DateTime']

del df['Serial']

df.plot(figsize=(15, 6))
plt.show()



