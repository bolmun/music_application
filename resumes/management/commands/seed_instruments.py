from django.core.management.base import BaseCommand
from resumes.models import instrumentChoice as r_instruments
from advertisements.models import instrumentChoice as a_instruments


class Command(BaseCommand):

    help = "This command helps to create instruments"

    def handle(self, *args, **options):
        instruments = [
            "Violin",
            "Viola",
            "Cello",
            "Double Bass",
            "Harp",
            "Flute",
            "Piccolo",
            "Oboe",
            "English Horn",
            "Clarinet",
            "Bass Clarinet",
            "Bassoon",
            "Contrabassoon",
            "Saxophone",
            "Trumpet",
            "Trombone",
            "Bass Trombone",
            "French Horn",
            "Tuba",
            "Timpani",
            "Snare Drum",
            "Bass Drum",
            "Triangle",
            "Gong",
            "Cymbals",
            "Vibraphone",
            "Piano",
        ]
        for i in instruments:
            r_instruments.objects.create(title=i)
            a_instruments.objects.create(title=i)
        self.stdout.write(
            self.style.SUCCESS(f"{len(instruments)} Instruments created!")
        )
