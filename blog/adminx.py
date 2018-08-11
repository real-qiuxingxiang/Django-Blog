from blog.models import *
import xadmin
from xadmin import views
from comments.models import Comment


class GlobalSetting(object):
    site_title = 'Q\'s BLog'
    site_footer = 'Copyright 2013 - 2018 by Q.'

    def get_site_menu(self):
        return (
            {'title': 'Blog', 'perm': self.get_model_perm(Blog, 'change'), 'menus': (
                {'title': 'Blog', 'url': self.get_model_url(Blog, 'changelist')},
                {'title': 'Tag', 'url': self.get_model_url(Tag, 'changelist')},
                {'title': 'Comment', 'url': self.get_model_url(Comment, 'changelist')},
            )},
        )

    def get_nav_menu(self):
        # 直接返回新增的菜单栏，源码中还有很大一部分的合并功能
        site_menu = list(self.get_site_menu() or [])
        return site_menu


class BlogAdmin(object):
    list_display = ('id', 'title', 'views', 'tags_list', 'created_time')
    list_display_links = ('title',)
    list_per_page = 20
    ordering = ('-created_time',)
    list_filter = ('tags',)
    readonly_fields = ['views']
    search_fields = ('title',)

    @staticmethod
    def tags_list(blog):
        tags = map(lambda x: x.name, blog.tags.all())
        return ', '.join(tags)


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Tag)
xadmin.site.register(Comment)
