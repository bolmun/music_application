import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from reviews import models as review_models
from resumes import models as resume_models


class Command(BaseCommand):

    help = "This command helps to create reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many reviews you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        resumes = resume_models.Resume.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(1, 5),
                "communication": lambda x: random.randint(1, 5),
                "professionailsm": lambda x: random.randint(1, 5),
                "kindness": lambda x: random.randint(1, 5),
                "user": lambda x: random.choice(all_users),
                "resume": lambda x: random.choice(resumes),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
