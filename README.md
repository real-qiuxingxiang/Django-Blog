# Django Blog

基于 Django 开发的博客系统:

- Python 3.6.6 和 Django 2.1.4
- MySQL
- [xadmin](https://github.com/sshwsfc/xadmin) 后台管理
- [Simditor Markdown](https://github.com/istommao/django-simditor) 编辑器，图片 Drag and Drop 上传
- 代码高亮
- RSS订阅
- 标签、阅读量
- [haystack](https://github.com/django-haystack/django-haystack) 文章内容搜索
- [Valine](https://github.com/xCss/Valine) 评论系统
- 集成 django-compressor，静态文件压缩

Usage:

- 新建虚拟环境

```
git clone git@github.com:chiuxingxiang/Django-Blog.git
virtualenv --python=<py3path> venv
. venv/bin/activate
```

- 安装依赖

```
pip install -r requirements.txt
```

- 数据库迁移

```
python manage.py makemigrations
python manage.py migrate
```

- 创建管理员

```
python manage.py shell  
from django.contrib.auth.models import User  
user=User.objects.create_superuser('用户名','邮箱','密码')
```

- 创建搜索索引

```
python manage.py rebuild_index
```

- 压缩静态文件

```
python manage.py collectstatic
python manage.py compress
```
------

### 首页

![index](/github_pic/index.png)

### 详情页 + 评论

![detail](/github_pic/detail.png)

### Tag List

![tag_list](/github_pic/tag.png)

### xadmin后台

![admin](/github_pic/admin.png)

### Simditor Markdown 文章编辑器 图片上传

![pic_upload](/github_pic/pic_upload.png)
