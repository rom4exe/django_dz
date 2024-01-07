import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for ph in phones:
            # TODO: Добавьте сохранение модели
            Phone.objects.create(
                name=ph['name'],
                price=ph['price'],
                image=ph['image'],
                release_date=ph['release_date'],
                lte_exists=ph['lte_exists'],
                slug=slugify(ph['name']),
            )