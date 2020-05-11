from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command helps to create amenities"

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Bathroom",
            "Carbon monoxide detectors",
            "CCTV",
            "Chair",
            "Convenience Store",
            "Cookware & Kitchen Utensils",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Hair Dryer",
            "Heating",
            "Laundromat",
            "Microwave",
            "Mini Bar",
            "Music Stand",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Toilet",
            "Towels",
            "Water Purifier",
        ]
        for a in amenities:
            Amenity.objects.create(title=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
