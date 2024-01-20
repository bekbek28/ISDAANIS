from django.core.management.base import BaseCommand
from faker import Faker
from Analytics.models import DailyTransaction, Species, Origin, Vessel, unloadType  

class Command(BaseCommand):
    help = 'Generate dummy data for DailyTransaction model.'

    def handle(self, *args, **options):
        fake = Faker()

        # Number of records you want to create
        num_records = 200

        # Check if the lists are not empty before proceeding
        species_ids = Species.objects.values_list('id', flat=True)
        origin_ids = Origin.objects.values_list('id', flat=True)
        vessel_ids = Vessel.objects.values_list('id', flat=True)
        unload_type_ids = unloadType.objects.values_list('id', flat=True)

        if not species_ids or not origin_ids or not vessel_ids or not unload_type_ids:
            self.stdout.write(self.style.ERROR('One or more of the required IDs lists is empty. Aborting data generation.'))
            return

        for _ in range(num_records):
            # Get random IDs
            species_id = fake.random_element(species_ids)
            origin_id = fake.random_element(origin_ids)
            vessel_id = fake.random_element(vessel_ids)
            unload_type_id = fake.random_element(unload_type_ids)

            # Create DailyTransaction instance with Faker data
            DailyTransaction.objects.create(
                species_id=species_id,
                origin_id=origin_id,
                vessel_id=vessel_id,
                unloadType_id=unload_type_id,  # Use the correct field name
                quantity=fake.random_int(min=50, max=200),
                date=fake.date_between(start_date='-5y', end_date='today'),
            )

        self.stdout.write(self.style.SUCCESS(f'{num_records} DailyTransaction records created successfully.'))
