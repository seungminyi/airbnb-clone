from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from rooms import models as room_model
from users import models as user_model

import random


class Command(BaseCommand):

    help = "Fake Room 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 방 생성할지 넘겨주는 인자"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        all_user = user_model.User.objects.all()
        room_types = room_model.RoomType.objects.all()
        seeder.add_entity(
            room_model.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_user),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(0, 300),
                "guests": lambda x: random.randint(0, 20),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        created_rooms_pk = seeder.execute()
        clean_create_rooms_pk = flatten(list(created_rooms_pk.values()))
        for pk in clean_create_rooms_pk:
            room = room_model.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_model.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,31)}.webp",
                )
        self.stdout.write(self.style.SUCCESS(f"{number} Room Created!"))
