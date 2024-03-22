import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df = pd.read_csv('data/real_madrid_playing_time.csv', header=[1])

age_threshold = 23

players_under_age_threshold = df[df['Age'] <= age_threshold]
players_over_age_threshold = df[df['Age'] > age_threshold]


players_counts = pd.Series([len(players_under_age_threshold), len(players_over_age_threshold)], index=['Under 23', 'Over 23'])


plt.figure(figsize=(8, 6))
players_counts.plot(kind='bar', color=['blue', 'red'])
plt.xlabel('Age Group')
plt.ylabel('Number of Players')
plt.title('Players by Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()