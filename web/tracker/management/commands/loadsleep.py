import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from tracker import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(args[0]) as csvfile:
            event = models.Event.objects.get(title='Sleep')
            event.entries.all().delete()
            entries = []
            rows = list(csv.reader(csvfile))[1:]
            for date, time, end, delta, note in rows:
                dt = '{} {}'.format(date, time)
                dt = datetime.strptime(dt, '%y/%m/%d %H:%M')
                t = float(delta) * 60
                entry = models.Entry(datetime=dt, event=event, duration=t)
                entries.append(entry)
        models.Entry.objects.bulk_create(entries)
