from .models import *


def data(request):
    content = {
        'menuData': Menu.objects.prefetch_related('submenu_set').all()
    }
    return content

