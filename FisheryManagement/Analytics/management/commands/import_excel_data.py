import pandas as pd
from django.core.management.base import BaseCommand
from Analytics.models import DailyTransaction, Species, Origin, Vessel

class Command(BaseCommand):
    help = 'Import data from multiple Excel files to Django models'

    def add_arguments(self, parser):
        parser.add_argument('excel_files', nargs='+', type=str, help='Paths to the Excel files')

    def handle(self, *args, **options):
        excel_file_paths = options['excel_files']

        for excel_file_path in excel_file_paths:
            # Read the Excel file into a pandas DataFrame
            df = pd.read_excel(excel_file_path)

            # Iterate through rows and create/update model instances
            for index, row in df.iterrows():
                DailyTransaction.objects.update_or_create(
                    unique_field=row['unique_field'],  # Replace with the actual unique field
                    defaults={
                        'field1': row['field1'],
                        'field2': row['field2'],
                        # Add other fields as needed
                    }
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

