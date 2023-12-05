from django.http import HttpResponseForbidden

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("No tienes permisos para acceder a esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
