import pandas as pd
from django.core.management.base import BaseCommand
from Analytics.models import DailyTransaction, Species, Origin, Vessel


class Command(BaseCommand):
    help = 'Load data from Excel file into Django database'

    def handle(self, *args, **options):
        excel_files = ['VOLUME and PRICE of Fish Unloading per SPECIE 2022.xlsx','FISH UNLOADING per ORIGIN 2022.xlsx']
        sheet_name = 'Sheet1'  
        start_row = 4  
        for file in excel_files:
            df = pd.read_excel(file, sheet_name, skiprows=start_row)
            print(f"Data from {file}, Sheet: {sheet_name}:\n{df}")

            print("Column Names:", df.columns)

            self.import_species_data(df)

    def import_species_data(self, df):
        fish_names = df['SPECIES'].unique()

        for fish_name in fish_names:
            # Try to get an existing species with the same name
            existing_species = Species.objects.filter(species_name=fish_name).first()

            if existing_species:
                # Update the quantity if the species already exists
                existing_species.quantity += 1  # You might need to adjust this based on your data
                existing_species.save()
            else:
                # Create a new species if it doesn't exist
                species_instance = Species(species_name=fish_name, quantity=1)  # You might need to adjust this based on your data
                species_instance.save()

    
