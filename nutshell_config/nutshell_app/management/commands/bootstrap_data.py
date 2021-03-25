"""
Populate the ShoeType table with the following entries:
sneaker
boot
sandal
dress
other

Populate the ShoeColor table with the following entries:
Red
Orange
Yellow
Green
Blue
Indigo
Violet
White
Black
"""

from django.core.management.base import BaseCommand
from nutshell_config.nutshell_app.models import NSShoeType, NSShoeColor


class Command(BaseCommand):
    help = 'Create data for database: NSShoeType and NSShowColor'

    def add_arguments(self, parser):
        parser.add_argument(
            'style',
            nargs=5,
            choices=[
                'SNEAKER',
                'BOOT',
                'SANDAL',
                'DRESS',
                'OTHER'
            ]
        )
        parser.add_argument(
            'color_name',
            nargs=9,
            choices=[
                'RED',
                'ORANGE',
                'YELLOW',
                'GREEN',
                'BLUE',
                'INDIGO',
                'VIOLET',
                'BLACK',
                'WHITE'
            ]
        )

    def handle(self, *args, **options):
        for (k, v) in NSShoeType.TYPE_NAME_CHOICES:
            NSShoeType.objects.create(style=k)
        for (k, v) in NSShoeColor.COLOR_NAME_CHOICES:
            NSShoeColor.objects.create(color_name=k)

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully added newly created data to project database.'
            )
        )
