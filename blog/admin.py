from blog.models import *
from django.contrib import admin


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views', 'tags_list', 'created_time')
    list_display_links = ('title',)
    list_per_page = 20
    ordering = ('-created_time',)
    list_filter = ('tags',)
    readonly_fields = ['views']
    search_fields = ('title',)

    filter_horizontal = ('tags',)
    fieldsets = (
        ("base info", {'fields': ['title', 'author', 'tags']}),
        ("Content", {'fields': ['content']})
    )

    @staticmethod
    def tags_list(blog):
        tags = map(lambda x: x.name, blog.tags.all())
        return ', '.join(tags)


class TagAdmin(object):
    list_display = ('name',)


admin.site.register(Tag)
