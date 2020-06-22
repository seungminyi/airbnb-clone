from django.core.management.base import BaseCommand
from rooms import models as rooms_model

class Command(BaseCommand):
    
    help = "Fake Room 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", type=int, help="몇개의 방 생성할지 넘겨주는 인자"
        )
    
    def handle(self, *args, **options):
        number = options.get("number",1)
        print(number)