import django

if django.VERSION > (1, 8,):
    from collections import OrderedDict
else:
    from django.utils.datastructures import SortedDict as OrderedDict  # noqa

if django.VERSION > (1, 8,):
    from django.template.loader import render_to_string
else:
    from django.template.loader import render_to_string as _render_to_string
    from django.template import RequestContext

    # Wire the Django >= 1.8 API to the Django < 1.7 implementation.
    def render_to_string(template_name, context=None, request=None, using=None):
        assert using is None, "Multiple template engines required Django >= 1.8"
        return _render_to_string(template_name, context, RequestContext(request))

try:
    from urllib.parse import parse_qsl, urlparse, urlunparse
except ImportError:
    from urlparse import parse_qsl, urlparse, urlunparse  # noqa

try:
    import importlib
except ImportError:
    from django.utils import importlib  # noqa
