import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from reservations import models as reservation_models
from resumes import models as resume_models


class Command(BaseCommand):

    help = "This command helps to create reservations"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many resevations you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        resumes = resume_models.Resume.objects.all()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "student": lambda x: random.choice(all_users),
                "resume": lambda x: random.choice(resumes),
                "meeting_address": lambda x: seeder.faker.address(),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reservations created!"))
