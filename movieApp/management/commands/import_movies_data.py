# myapp/management/commands/import_movies_data.py
import csv
from django.core.management.base import BaseCommand
from movieApp.models import Movie
import re

class Command(BaseCommand):
    help = 'Import movies data from CSV file'

    def handle(self, *args, **options):
        # Adjust the file path accordingly
        Movie.objects.all().delete()
        
        csv_file_path = '/Users/sarafryzlewicz/Downloads/movieInfo/movies.csv'

        

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                movie_id = int(row[0])  # Assuming movieId is in the first column and is an integer
                title = row[1]
                genres_str = row[2]

                # Preprocess genres data (split by '|')
                genres_list = genres_str.split('|')

                match = re.search(r'\((\d{4})\)$', title)
                year = match.group(1) if match else None

                # Save to the database
                Movie.objects.create(movieId=movie_id, title=title, genres=genres_list)

        self.stdout.write(self.style.SUCCESS('Successfully imported movies data'))
