import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df = pd.read_csv('data/real_madrid_playing_time.csv', header=[1])

#print(tabulate(df, tablefmt='pipe', headers='keys'))

# Define a function to map nationality codes to simplified names
def map_nationality(nation_code):
    nationality_mapping = {
        'at AUT': 'Austria',
        'be BEL': 'Belgium',
        'br BRA': 'Brazil',
        'hr CRO': 'Croatia',
        'do DOM': 'Dominican Rep.',
        'es ESP': 'Spain',
        'fr FRA': 'France',
        'de GER': 'Germany',
        'uy URU': 'Uruguay',
        'ua UKR': 'Ukraine',
        'rs SRB': 'Serbia',
        'wls WAL': 'Wales'
    }
    return nationality_mapping.get(nation_code, nation_code)

# Apply the mapping function to create a new column for simplified nationalities (for plotting purposes)
df['Simplified_Nation'] = df['Nation'].apply(map_nationality)

# Count the occurrences of each simplified nationality
nationality_counts = df['Simplified_Nation'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
nationality_counts.plot(kind='bar', color='blue')
plt.xlabel('Nationality')
plt.ylabel('Number of Players')
plt.title('Players by Nationality')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()