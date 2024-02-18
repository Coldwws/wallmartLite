from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin

class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'parent')
    list_display_links = ('indented_title',)
    ordering = ('tree_id', 'level', 'lft')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(ProductImage)