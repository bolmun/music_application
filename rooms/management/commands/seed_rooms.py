import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command helps to create rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_types": lambda x: random.choice(room_types),
                "capacity": lambda x: random.randint(1, 20),
                "price_per_hour": lambda x: random.randint(1000, 50000),
            },
        )

        created_rooms = seeder.execute()
        created_clean = flatten(list(created_rooms.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.Rule.objects.all()
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 20)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1,20)}.webp",
                    room=room,
                )
            for a in amenities:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.amenities.add(a)

            for f in facilities:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.facilities.add(f)

            for r in rules:
                magic_number = random.randint(0, 10)
                if magic_number % 2 == 0:
                    room.rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
