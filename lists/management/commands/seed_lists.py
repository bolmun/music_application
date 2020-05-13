import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from lists import models as list_models
from resumes import models as resume_models


class Command(BaseCommand):

    help = "This command helps to create lists"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many lists you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        resumes = resume_models.Resume.objects.all()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(all_users),},
        )

        created_resume = seeder.execute()
        cleaned_resume = flatten(list(created_resume.values()))
        for pk in cleaned_resume:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = resumes[random.randint(0, 5) : random.randint(6, 30)]
            list_model.resumes.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
