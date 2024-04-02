from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return HttpResponse("Hello, world. You're at the football index.")


def my_diagrams(request):
    # Load football data using the CSV file path from settings.py
    csv_file_path = settings.CSV_FILE_PATH
    df = pd.read_csv(csv_file_path, header=[1])

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

    # Apply the mapping function to create a new column for simplified nationalities
    df['Simplified_Nation'] = df['Nation'].apply(map_nationality)

    # Data processing and plotting for the first diagram
    nationality_counts = df['Simplified_Nation'].value_counts()
    plt.figure(figsize=(8, 6))
    nationality_counts.plot(kind='bar', color='blue')
    plt.xlabel('Nationality')
    plt.ylabel('Number of Players')
    plt.title('Players by Nationality (Real Madrid)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    plt.close()
    diagram_image1 = base64.b64encode(buffer1.getvalue()).decode('utf-8')

    # Data processing and plotting for the second diagram
    spanish_players_count = df[df['Simplified_Nation'] == 'Spain'].shape[0]
    other_players_count = df.shape[0] - spanish_players_count
    labels = ['Spanish Players', 'Other Players']
    sizes = [spanish_players_count, other_players_count]
    colors = ['red', 'green']
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, textprops={'color': 'black'})
    plt.title('Spanish Players vs Other Players (Real Madrid)')
    plt.tight_layout()
    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    plt.close()
    diagram_image2 = base64.b64encode(buffer2.getvalue()).decode('utf-8')

    # Data processing and plotting for the third diagram (pie chart)
    spanish_minutes = df[df['Simplified_Nation'] == 'Spain']['Min'].sum()
    other_minutes = df[df['Simplified_Nation'] != 'Spain']['Min'].sum()
    sizes = [spanish_minutes, other_minutes]
    colors = ['lightskyblue', 'lightcoral']
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Total Minutes Played by Spanish Players vs Other Players')
    plt.tight_layout()
    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    plt.close()
    diagram_image3 = base64.b64encode(buffer3.getvalue()).decode('utf-8')

    return render(request, 'ftbl/diagrams.html',
                  {'diagram_image1': diagram_image1,
                   'diagram_image2': diagram_image2,
                   'diagram_image3': diagram_image3})

