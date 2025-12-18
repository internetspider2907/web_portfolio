import os
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.conf import settings
from main.models import WorkImage


class Command(BaseCommand):
    help = 'Load image URLs from image_urls.txt and create WorkImage entries'

    def handle(self, *args, **options):
        path = settings.BASE_DIR / 'image_urls.txt'
        if not path.exists():
            self.stdout.write(self.style.ERROR(f'{path} not found'))
            return

        with open(path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f if l.strip() and not l.strip().startswith('#')]

        for i, url in enumerate(lines, start=1):
            try:
                r = requests.get(url, timeout=20)
                r.raise_for_status()
                ext = os.path.splitext(url)[1] or '.jpg'
                name = f'bulk_{i}{ext}'
                wi = WorkImage(title=name)
                wi.image.save(name, ContentFile(r.content), save=True)
                self.stdout.write(self.style.SUCCESS(f'Imported {url}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed {url}: {e}'))
