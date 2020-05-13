import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from reports import models as report_models


class Command(BaseCommand):

    help = "This command helps to create reports"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reports you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            report_models.Report,
            number,
            {
                "student": lambda x: random.choice(all_users),
                "instructor": lambda x: random.choice(all_users),
                "achievement_score": lambda x: random.randint(0, 100),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reports created!"))
