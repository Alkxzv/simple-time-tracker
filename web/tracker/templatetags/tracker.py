from django import template
from django.template.defaultfilters import stringfilter

from tracker.models import PRO

PRO_DICT = dict(PRO)

register = template.Library()


@register.filter
def hours(minutes):
    if not minutes:
        return '~'
    elif minutes < 180:
        return "{:.0f}'".format(minutes)
    elif minutes / 60 < 20:
        return "{:.1f}h".format(minutes / 60)
    else:
        return "{:.0f}h".format(minutes / 60)


@register.filter(is_safe=True)
def stars(rating):
    stars = ''
    if rating is None:
        return '~'
    while rating >= 1:
        rating -= 1
        stars += '●'
    if rating >= 0.75:
        stars += '●'
    elif rating >= 0.25:
        stars += '◐'
    while len(stars) < 5:
        stars += '○'
    return stars


@register.filter
def icon(progress):
    return PRO_DICT.get(progress, '~')


@register.filter
def article(string):
    if string[-3:] == ", A":
        string = "A " + string[:-3]
    elif string[-4:] == ", An":
        string = "An " + string[:-4]
    elif string[-5:] == ", The":
        string = "The " + string[:-5]
    elif string[-8:] == ", On the":
        string = "On the " + string[:-8]
    elif string[-4:] == ", El":
        string = "El " + string[:-4]
    elif string[-4:] == ", La":
        string = "La " + string[:-4]
    return string
