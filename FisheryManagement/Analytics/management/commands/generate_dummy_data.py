from django.core.management.base import BaseCommand
from faker import Faker
from Analytics.models import DailyTransaction, Species, Origin, Vessel

class Command(BaseCommand):
    help = 'Generate dummy data for DailyTransaction model.'

    def handle(self, *args, **options):
        fake = Faker()

        # Number of records you want to create
        num_records = 300

        # Get the IDs of existing Species, Origin, and Vessel instances to use in ForeignKeys
        species_ids = Species.objects.values_list('id', flat=True)
        origin_ids = Origin.objects.values_list('id', flat=True)
        vessel_ids = Vessel.objects.values_list('id', flat=True)

        for _ in range(num_records):
            # Replace the following code with the logic to create instances of DailyTransaction
            # using the Faker library to populate fields with random data.
            # For example:
            DailyTransaction.objects.create(
                species_id=fake.random_element(species_ids),
                origin_id=fake.random_element(origin_ids),
                vessel_id=fake.random_element(vessel_ids),
                quantity=fake.random_int(min=1, max=300),
                price=fake.random_int(min=10, max=1000),
                date=fake.date_between(start_date='-4y', end_date='today'),
            )

        self.stdout.write(self.style.SUCCESS(f'{num_records} DailyTransaction records created successfully.'))
