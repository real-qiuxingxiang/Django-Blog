from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from .models import *
from comments.forms import CommentForm


# def blog_detail(request, id):
#    blog = get_object_or_404(Blog, id=id)
#    blog.count_views()
#    return render(request, 'blog.html', context={'blog': blog})


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        blog = super(BlogDetailView, self).get_object()
        blog.count_views()
        return blog

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tag.html'


class TagDetailView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'tag_detail.html'

    def get_queryset(self):
        tag = get_object_or_404(Tag, id=self.kwargs.get('id'))
        return super(TagDetailView, self).get_queryset().filter(tags=tag)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, id=self.kwargs.get('id'))
        context['tag_name'] = tag.name
        return context


class RSSFeed(Feed):
    title = "Q's Blog"
    link = "feeds/"
    description = "RSS feed - blog posts"

    @staticmethod
    def items():
        return Blog.objects.order_by('-created_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content
