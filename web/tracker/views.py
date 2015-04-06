from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
import datetime as dt
import json

from . import models, forms
from .nvd3 import (duration_chart_data, duration_weekday_chart_data,
                   duration_monthly_chart_data, duration_yearly_chart_data)
from common.views import LoginMixin, SiteMixin


class MainView(LoginMixin, SiteMixin, TemplateView):
    template_name = 'tracker/main.html'
    section = 'tracker'

    def get_context_data(self):
        context = super().get_context_data()
        events = models.Event.objects.filter(progress=3).annotate_duration()
        context['pending_events'] = events.order_by('-duration')
        events = models.Event.objects.filter(progress=4).annotate_duration()
        context['ongoing_events'] = events.order_by('-duration')
        entries = models.Entry.objects.filter(duration=None)
        context['pending_entries'] = entries.order_by('-datetime')
        return context


class StatsView(LoginMixin, SiteMixin, TemplateView):
    template_name = 'tracker/stats.html'
    section = 'stats'

    def get_context_data(self):
        context = super().get_context_data()
        duration = models.Entry.objects.all().duration_over_time()
        duration_data = duration_weekday_chart_data(duration)
        context['weekday_data'] = json.dumps(duration_data)
        duration_data = duration_monthly_chart_data(duration)
        context['monthly_data'] = json.dumps(duration_data)
        duration_data = duration_yearly_chart_data(duration)
        context['yearly_data'] = json.dumps(duration_data)
        # This time n years ago
        context['n_years_ago'] = []
        today = dt.date.today()
        delta = dt.timedelta(3)
        for year in range(today.year - 1, 2007, -1):
            start = dt.datetime(year, today.month, today.day, 0, 0) - delta
            end = dt.datetime(year, today.month, today.day, 23, 59) + delta
            entries = models.Entry.objects.filter(datetime__range=(start, end))
            if entries:
                context['n_years_ago'].append((year, entries))
        return context


# Entries

class EntryMixin(LoginMixin, SiteMixin):
    model = models.Entry
    section = 'entries'


class EntryView(EntryMixin, DetailView):
    pass


class EntryCreateView(EntryMixin, CreateView):
    fields = 'datetime', 'event', 'duration', 'annotation'

    def get_initial(self):
        try:
            event_pk = self.request.GET.get('event')
            event = models.Event.objects.get(id=event_pk)
            initial = {'event': event}
        except models.Event.DoesNotExist:
            initial = {}
        finally:
            initial['datetime'] = timezone.now()
        return initial


class EntryUpdateView(EntryMixin, UpdateView):
    fields = 'datetime', 'event', 'duration', 'annotation'


class EntryListView(EntryMixin, ListView):
    queryset = models.Entry.objects.all().select_related('event')
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = context['object_list']
        if object_list is not None:
            duration = object_list.duration_over_time()
            duration_data = duration_chart_data(duration)
            context['duration_data'] = json.dumps(duration_data)
        return context


class EntryCloseView(EntryMixin, UpdateView):

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        delta = timezone.now() - instance.datetime
        instance.duration = int(delta.days * 24 * 60 + delta.seconds / 60)
        instance.save()
        url = reverse('tracker:events:detail', args=[instance.event.id])
        return HttpResponseRedirect(url)


# Events

class EventMixin(LoginMixin, SiteMixin):
    model = models.Event
    section = 'events'


class EventView(EventMixin, DetailView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        entries = self.object.entries.all()
        context['entry_list'] = entries.order_by('-datetime')
        context['tag_list'] = self.object.tags.all().order_by('value')
        duration = entries.duration_over_time()
        context['duration_data'] = json.dumps(duration_chart_data(duration))
        return context


class EventCreateView(EventMixin, CreateView):
    form_class = forms.EventForm


class EventUpdateView(EventMixin, UpdateView):
    form_class = forms.EventForm


class EventListView(EventMixin, ListView):
    paginate_by = 100
    queryset = models.Event.objects.all()\
        .annotate_duration().order_by('-date')


# Tags

class TagMixin(LoginMixin, SiteMixin):
    model = models.Tag
    section = 'tags'


class TagView(TagMixin, DetailView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        events = self.object.events.all().annotate_duration()
        context['event_list'] = events.order_by('-rating')
        entries = models.Entry.objects.filter(event__in=events)
        entries = entries.select_related('event')
        context['entry_list'] = entries.order_by('-datetime')
        duration = entries.duration_over_time()
        duration_data = duration_monthly_chart_data(duration)
        context['duration_data'] = json.dumps(duration_data)
        return context


class TagListView(TagMixin, ListView):
    queryset = models.Tag.objects.all().annotate_duration().annotate_rating()\
        .order_by('-duration')
    paginate_by = 100
