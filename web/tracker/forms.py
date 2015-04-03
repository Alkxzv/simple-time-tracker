from django import forms

from . import models

HT = 'Write tags, separated by semicolon.'


class EventForm(forms.ModelForm):
    add_tags = forms.CharField(max_length=100, help_text=HT, required=False)
    remove_tags = forms.CharField(max_length=100, help_text=HT, required=False)

    class Meta:
        model = models.Event
        fields = 'title', 'description', 'date', 'progress', 'rating'

    def clean_add_tags(self):
        return [v.strip() for v in self.cleaned_data['add_tags'].split(';')]

    def clean_remove_tags(self):
        return [v.strip() for v in self.cleaned_data['remove_tags'].split(';')]

    def save(self, *args, **kwargs):
        event = super().save(*args, **kwargs)
        for value in self.cleaned_data['remove_tags']:
            try:
                tag = event.tags.get(value=value)
            except models.Tag.DoesNotExist:
                tag = None
            else:
                event.tags.remove(tag)
        for value in self.cleaned_data['add_tags']:
            if value:
                tag, created = models.Tag.objects.get_or_create(value=value)
                event.tags.add(tag)
        return event
