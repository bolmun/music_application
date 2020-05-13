import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from resumes import models as resume_models


class Command(BaseCommand):

    help = "This command helps to create resumes"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many resumes you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        instrument = resume_models.instrumentChoice.objects.all()
        seeder.add_entity(
            resume_models.Resume,
            number,
            {
                "resume_title": lambda x: seeder.faker.sentence(),
                "instructor": lambda x: random.choice(all_users),
                "instrument": lambda x: random.choice(instrument),
                "fee": lambda x: random.randint(30000, 100000),
            },
        )

        created_resumes = seeder.execute()
        created_clean = flatten(list(created_resumes.values()))
        for pk in created_clean:
            resume = resume_models.Resume.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                resume_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"profile_pics/{random.randint(1,20)}.webp",
                    resume=resume,
                )

        self.stdout.write(self.style.SUCCESS(f"{number} resumes created!"))
