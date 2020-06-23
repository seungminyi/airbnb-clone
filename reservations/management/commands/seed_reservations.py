import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models
from reservations import models as reservation_models

NAME = "reservations"


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
            reservation_models.Reservation,
            number,
            {
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} Created"))
