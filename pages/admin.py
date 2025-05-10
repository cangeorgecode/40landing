from django.contrib import admin
from .models import Page, Section, FAQ

admin.site.register(Page)
admin.site.register(Section)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('page', 'question', 'order')
    list_filter = ('page',)
    ordering = ('page', 'order',)
    search_fields = ('question', 'answer')