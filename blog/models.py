from django.db import models
from django.contrib.auth.models import User
from simditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField('标签', max_length=20, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '标签'

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField('标题', max_length=50)
    content = RichTextField('内容')
    created_time = models.DateTimeField('创建日期')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = verbose_name = '文章'
        ordering = ['-created_time']

    def count_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return "/blog/" + str(self.id)

    def pre_blog(self):
        return Blog.objects.filter(id__lt=self.id).first()

    def next_blog(self):
        return Blog.objects.filter(id__gt=self.id).first()

    def __str__(self):
        return self.title
