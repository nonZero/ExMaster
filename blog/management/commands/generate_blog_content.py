from django.core.management.base import BaseCommand
from blog import models
import silly


class Command(BaseCommand):
    help = "Generate silly content for blog"

    def handle(self, *args, **options):
        for i in range(10):
            p = models.Post(
                title=silly.sentence(),
                content=silly.markdown(length=5),
            )
            p.save()
