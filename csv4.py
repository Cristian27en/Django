import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df = pd.read_csv('data/real_madrid_playing_time.csv', header=[1])

players_group = df.groupby('Pos')

print(players_group)

for position, group in players_group:
    print(f"Posn: {position}")
    print(group)
    print()

players_count_by_position = df.groupby('Pos').size()

plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
players_count_by_position.plot(kind='bar', color='skyblue')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.title('Number of Players by Position')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()