import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from store_data_app.models import StoreStatus, BusinessHours, Timezones

class Command(BaseCommand):
    help = 'Import data from CSV files into the database'

    def handle(self, *args, **options):
        # Import StoreStatus data
        print('1-->storing store status data........')
        with open('store_status.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                store_id, status, timestamp_utc = row

                # Convert timestamp_utc to the correct DateTime format
                timestamp_dt = datetime.strptime(timestamp_utc, '%Y-%m-%d %H:%M:%S.%f %Z')
                
                StoreStatus.objects.create(
                    store_id=store_id,
                    status=status,
                    timestamp_utc=timestamp_dt
                )
        print('store status data DONE')

        #  BusinessHours data
        print('2-->storing BusinessHours data........')
        with open('business_hours.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                store_id, day, start_time_local, end_time_local = row
                BusinessHours.objects.create(
                    store_id=store_id,
                    day=day,
                    start_time_local=start_time_local,
                    end_time_local=end_time_local
                )
        print('BusinessHours data DONE')

        # Timezones data
        print('3-->storing Timezones data data........')
        with open('timezones.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                store_id, timezone_str = row
                Timezones.objects.create(
                    store_id=store_id,
                    timezone_str=timezone_str
                )
        print('Timezones data DONE')
