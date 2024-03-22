import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df = pd.read_csv('data/real_madrid_playing_time.csv', header=[1])

#print(df.head())
#print(tabulate(df))
print(tabulate(df, tablefmt='pipe', headers='keys'))

players_from_spain = df[df['Nation'] == 'es ESP']
#print(tabulate(players_from_spain, tablefmt='pipe', headers='keys'))
#print(players_from_spain)
#players_age_u23 = df[df['Age'] <= '23.0']


