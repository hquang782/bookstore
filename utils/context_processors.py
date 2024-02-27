from catalog.models import Category
from bookstore import settings

def bookstore(request):
    return {
        'active_categories': Category.objects.using('mongodb').filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }