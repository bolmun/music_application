from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command helps to create facilities"

    def handle(self, *args, **options):
        facilities = [
            "Drum",
            "Elevator",
            "Music Stand",
            "Piano",
            "Paid parking on premises",
            "Paid parking off premises",
            "Window",
        ]
        for f in facilities:
            Facility.objects.create(title=f)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))
