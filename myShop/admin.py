from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'status']
    prepopulated_fields = {'slug': ('menu_name',)}
    search_fields = ['menu_name']
    actions = ['update_menu_status_active', 'update_menu_status_inactive']

    def update_menu_status_active(self, request, query):
        query.update(status=True)

    update_menu_status_active.short_description = 'Active'

    def update_menu_status_inactive(self, request, query):
        query.update(status=False)

    update_menu_status_inactive.short_description = 'Inactive'


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    actions = ['update_submenu_status_active', 'update_submenu_status_inactive']

    def update_submenu_status_active(self, request, query):
        query.update(status=True)

    update_submenu_status_active.short_description = 'Active'

    def update_submenu_status_inactive(self, request, query):
        query.update(status=False)

    update_submenu_status_inactive.short_description = 'Inactive'


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'status']
    prepopulated_fields = {'slug': ('item_name',)}
    search_fields = ['item_name']
    actions = ['update_item_status_active', 'update_item_status_inactive']

    def update_item_status_active(self, request, query):
        query.update(status=True)

    update_item_status_active.short_description = 'Active'

    def update_item_status_inactive(self, request, query):
        query.update(status=False)

    update_item_status_inactive.short_description = 'Inactive'


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['update_slider_status_active', 'update_slider_status_inactive']

    def update_slider_status_active(self, request, query):
        query.update(status=True)

    update_slider_status_active.short_description = 'Active'

    def update_slider_status_inactive(self, request, query):
        query.update(status=False)

    update_slider_status_inactive.short_description = 'Inactive'
