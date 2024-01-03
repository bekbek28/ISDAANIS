from django.core.management.base import BaseCommand
from faker import Faker
from Analytics.models import DailyTransaction, Species, Origin, Vessel

class Command(BaseCommand):
    help = 'Generate dummy data for DailyTransaction model.'

    def handle(self, *args, **options):
        fake = Faker()

        # Number of records you want to create
        num_records = 40

        # Get the IDs of existing Species, Origin, and Vessel instances to use in ForeignKeys
        species_ids = Species.objects.values_list('id', flat=True)
        origin_ids = Origin.objects.values_list('id', flat=True)
        vessel_ids = Vessel.objects.values_list('id', flat=True)

        # Check if the lists are not empty before proceeding
        if not species_ids or not origin_ids or not vessel_ids:
            self.stdout.write(self.style.ERROR('One or more of the required IDs lists is empty. Aborting data generation.'))
            return

        for _ in range(num_records):
            # Get random IDs
            species_id = fake.random_element(species_ids)
            origin_id = fake.random_element(origin_ids)
            vessel_id = fake.random_element(vessel_ids)

            # Create DailyTransaction instance
            DailyTransaction.objects.create(
                species_id=species_id,
                origin_id=origin_id,
                vessel_id=vessel_id,
                quantity=fake.random_int(min=100, max=300),
                date=fake.date_between(start_date='-4y', end_date='today'),
            )

        self.stdout.write(self.style.SUCCESS(f'{num_records} DailyTransaction records created successfully.'))
