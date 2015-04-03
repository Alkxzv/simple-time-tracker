from collections import OrderedDict, defaultdict
import datetime as dt
import time


def line_chart_data(data, key):
    t = lambda t: time.mktime(t.timetuple()) * 1000
    d = lambda d: d / 60
    values = [{'x': t(k), 'y': d(v)} for k, v in data.items()]
    return [{
        'key': key,
        'values': sorted(values, key=lambda v: v['x']),
    }]


def duration_chart_data(data):
    t = lambda t: time.mktime(t.timetuple()) * 1000
    if len(data) > 1:
        start, end = min(data.keys()), max(data.keys())
        datum = OrderedDict()
        while start <= end:
            datum[t(start)] = 0
            start += dt.timedelta(days=1)
        for date, value in data.items():
            datum[t(date)] += value / 60
        return [{
            'key': 'Duration',
            'bar': True,
            'values': list(datum.items()),
        }]
    else:
        return []


def duration_monthly_chart_data(data):
    month = lambda d: dt.date(d.year, d.month, 1)
    t = lambda t: time.mktime(t.timetuple()) * 1000
    if len(data) > 1:
        start, end = min(data.keys()), max(data.keys())
        datum = OrderedDict()
        while start <= end:
            datum[t(month(start))] = 0
            start += dt.timedelta(days=1)
        for date, value in data.items():
            datum[t(month(date))] += value / 60
        return [{
            'key': 'Duration',
            'bar': True,
            'values': list(datum.items()),
        }]
    else:
        return []


def duration_yearly_chart_data(data):
    year = lambda d: dt.date(d.year, 1, 1)
    t = lambda t: time.mktime(t.timetuple()) * 1000
    if len(data) > 1:
        start, end = min(data.keys()), max(data.keys())
        datum = OrderedDict()
        while start <= end:
            datum[t(year(start))] = 0
            start += dt.timedelta(days=1)
        for date, value in data.items():
            datum[t(year(date))] += value / 60
        return [{
            'key': 'Duration',
            'bar': True,
            'values': list(datum.items()),
        }]
    else:
        return []


def duration_weekday_chart_data(data):
    t = lambda t: time.mktime(t.timetuple()) * 1000
    if len(data) > 1:
        start, end = min(data.keys()), max(data.keys())
        datum = OrderedDict()
        while start <= end:
            datum[start.weekday()] = 0
            start += dt.timedelta(days=1)
        for date, value in data.items():
            datum[date.weekday()] += value / 60
        return [{
            'key': 'Duration',
            'bar': True,
            'values': sorted(list(datum.items())),
        }]
    else:
        return []
