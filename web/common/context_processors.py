from django.conf import settings


def common_context(request):
    context = settings.COMMON_CONTEXT
    return context
