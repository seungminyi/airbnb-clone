from django.core.management.base import BaseCommand
from rooms import models as rooms_model

class Command(BaseCommand):
    help = "Facilities 생성"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            rooms_model.Facility.objects.create(name=f)
            self.stdout.wirte(self.style.SUCCESS("Facilities FakeData Create"))