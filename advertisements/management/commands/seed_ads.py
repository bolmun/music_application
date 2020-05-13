import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from advertisements import models as ad_models


class Command(BaseCommand):

    help = "This command helps to create students' advertisement"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many ads you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        instrument = ad_models.instrumentChoice.objects.all()
        seeder.add_entity(
            ad_models.Advertisement,
            number,
            {
                "student": lambda x: random.choice(all_users),
                "instrument": lambda x: random.choice(instrument),
                "min_fee": lambda x: random.randint(10000, 30000),
                "max_fee": lambda x: random.randint(30000, 100000),
            },
        )

        created_ads = seeder.execute()
        created_clean = flatten(list(created_ads.values()))
        desired_lesson_days = ad_models.LessonDay.objects.all()
        lesson_type = ad_models.LessonType.objects.all()
        prefer_style = ad_models.PreferStyle.objects.all()

        for pk in created_clean:
            advertisement = ad_models.Advertisement.objects.get(pk=pk)

            for d in desired_lesson_days:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    advertisement.desired_lesson_days.add(d)

            for t in lesson_type:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    advertisement.lesson_type.add(t)

            for p in prefer_style:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    advertisement.prefer_style.add(p)

        self.stdout.write(self.style.SUCCESS(f"{number} students' ads created!"))
