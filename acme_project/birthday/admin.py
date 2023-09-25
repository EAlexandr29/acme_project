from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'image',
    )

    search_fields = ('first_name', 'last_name')
    list_display_links = ('first_name', 'last_name')


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )

    search_fields = ('tag',)
    list_display_links = ('tag',)


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)
