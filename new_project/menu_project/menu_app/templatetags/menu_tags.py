from django import template
from ..models import Menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return ''

    return menu.menuitem_set.all()
