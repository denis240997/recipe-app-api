import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


# This is bullshit! Problem was not solved! 
# The first connection is successful, but after that postgres closes the connection and 
# reconnects. At the moment, this script has already worked, so the application container crashes.
class Command(BaseCommand):
    '''Django command to pause execution until database is avaliable'''

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_connection = None
        while not db_connection:
            try:
                time.sleep(2)    # ha-ha, yes! it's just a delay for the database to start up
                db_connection = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is up!'))
