from collections import defaultdict
from django.core.urlresolvers import reverse
from django.db import models
import datetime as dt

PRO = (
    (None, "~"),
    (1, "Finished"),
    (2, "Stopped"),
    (3, "Pending"),
    (4, "Ongoing"),
)

RAT = (
    (None, "~"),
    (0, "○○○○○ Terrible"),
    (1, "●○○○○ Poor"),
    (2, "●●○○○ Okay"),
    (3, "●●●○○ Good"),
    (4, "●●●●○ Great"),
    (5, "●●●●● Excellent"),
)


# Entries

class EntryQuerySet(models.query.QuerySet):

    def duration_over_time(self):
        datetime_sum = defaultdict(int)
        for datetime, duration in self.values_list('datetime', 'duration'):
            if duration and datetime >= dt.datetime(2010, 1, 1):
                datetime_sum[datetime.date()] += duration
        keys = datetime_sum.keys()
        if keys:
            d, end = min(keys), max(keys)
            while d <= end:
                datetime_sum[d] = datetime_sum.get(d, 0)
                d += dt.timedelta(days=1)
        return datetime_sum


class EntryManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return EntryQuerySet(self.model)


class Entry(models.Model):
    datetime = models.DateTimeField()
    event = models.ForeignKey('tracker.Event', related_name='entries')
    duration = models.SmallIntegerField(blank=True, null=True)
    annotation = models.TextField(blank=True)
    objects = EntryManager()

    class Meta:
        ordering = '-datetime',
        verbose_name_plural = "entries"

    def __str__(self):
        return '[{}] {}'.format(self.datetime, self.event.title)

    def get_absolute_url(self):
        return self.event.get_absolute_url()


# Events

class EventQuerySet(models.query.QuerySet):

    def annotate_duration(self):
        d = models.Sum('entries__duration')
        return self.annotate(duration=d)


class EventManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return EventQuerySet(self.model)


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    progress = models.SmallIntegerField(blank=True, null=True, choices=PRO)
    rating = models.SmallIntegerField(blank=True, null=True, choices=RAT)
    tags = models.ManyToManyField('tracker.Tag',
                                  blank=True,
                                  related_name='events')
    objects = EventManager()

    class Meta:
        unique_together = ('title', 'date'),
        ordering = '-date',

    def __str__(self):
        return '{} ({})'.format(self.title, self.date.year)

    def get_absolute_url(self):
        return reverse('tracker:events:detail', args=[self.pk])

    def get_duration(self):
        duration = self.entries.aggregate(sum=models.Sum('duration'))['sum']
        return 0 if duration is None else duration

    def entry_count(self):
        return self.entries.count()


# Tags

class TagQuerySet(models.query.QuerySet):

    def annotate_duration(self):
        d = models.Sum('events__entries__duration')
        return self.annotate(duration=d)

    def annotate_rating(self):
        r = models.Avg('events__rating')
        return self.annotate(rating=r)


class TagManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return TagQuerySet(self.model)


class Tag(models.Model):
    value = models.CharField(unique=True, max_length=20)
    objects = TagManager()

    class Meta:
        ordering = 'value',

    def __str__(self):
        return '[{}]'.format(self.value)

    def get_duration(self):
        aggregated = self.events.aggregate(sum=models.Sum('entries__duration'))
        duration = aggregated['sum']
        return 0 if duration is None else duration

    def get_rating(self):
        events = self.events.all().annotate(count=models.Count('entries'))
        total = sum(x.rating * x.count for x in events if x.rating)
        duration = sum(x.count for x in events if x.rating)
        return total / duration if duration > 0 else None

    def event_count(self):
        return self.events.count()

    def entry_count(self):
        events = self.events.all()
        return Entry.objects.filter(event__in=events).count()

    def get_absolute_url(self):
        return reverse('tracker:tags:detail', args=[self.pk])
