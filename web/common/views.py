from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SiteMixin:
    section = None
    sidebar = False

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['site_section'] = self.section
        context['site_sidebar'] = self.sidebar
        return context


def make_view_mixin(class_name, decorator):
    mixin = type(class_name, (object, ), {})

    def dispatch(self, *args, **kwargs):
        return super(mixin, self).dispatch(*args, **kwargs)

    mixin.dispatch = method_decorator(decorator)(dispatch)
    return mixin


GetMixin = make_view_mixin('GetMixin', require_GET)
LoginMixin = make_view_mixin('LoginMixin', login_required)
PostMixin = make_view_mixin('PostMixin', require_POST)


class AdminMixin(LoginMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(self, request, *args, **kwargs)


class UserMixin(LoginMixin):

    def dispatch(self, request, *args, **kwargs):
        try:
            object = self.get_object()
        except AttributeError:
            raise Http404(
                "Could not check permissions because no model was found."
            )
        else:
            if request.user.is_superuser or request.user == object.user:
                return super().dispatch(self, request, *args, **kwargs)
            else:
                raise PermissionDenied
