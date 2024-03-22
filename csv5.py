import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df = pd.read_csv('data/real_madrid_playing_time.csv', header=[1])

plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.scatter(df.index, df['Min'], color='blue', alpha=0.6)
plt.xlabel('Player Index')
plt.ylabel('Minutes Played')
plt.title('Minutes Played by Players')
plt.grid(True)  # Add grid lines

for i, player in enumerate(df['Player']):
    plt.text(i, df.loc[i, 'Min'], player, ha='left', va='bottom', fontsize=8, rotation=45, color='black', alpha=1)

plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()