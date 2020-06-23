from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten
from users import models as user_models
from rooms import models as room_models
from lists import models as list_models
import random

NAME = "list"


class Command(BaseCommand):

    help = f"{NAME} 생성"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1, help=f"생성 {NAME}수")

    def handle(self, *args, **options):
        number = options.get("number", 1)
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            list_models.List, number, {"user": lambda x: random.choice(users)},
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} Created"))
