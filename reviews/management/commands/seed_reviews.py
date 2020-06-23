from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from reviews import models as review_models
from rooms import models as room_models
import random


class Command(BaseCommand):

    help = "Review 생성"

    def add_arguments(self, parser):
        parser.add_argument("--number", type=int, default=1, help="생성 리뷰수")

    def handle(self, *args, **options):
        number = options.get("number", 1)
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews Created"))
