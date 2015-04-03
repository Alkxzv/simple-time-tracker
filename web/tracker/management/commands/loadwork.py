import csv
from datetime import datetime

from django.core.management.base import BaseCommand

from tracker import models


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(args[0]) as csvfile:
            event = models.Event.objects.get(title=args[1])
            event.entries.all().delete()
            entries = []
            rows = list(csv.reader(csvfile))[2:]
            for date, tbus, toff, tout, thome, dout, doff, dwork, *_ in rows:
                if toff:
                    dt = '{} {}'.format(date, toff.zfill(5))
                    dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')
                    t = float(dwork) * 60
                    entry = models.Entry(datetime=dt, event=event, duration=t)
                    entries.append(entry)
        models.Entry.objects.bulk_create(entries)
