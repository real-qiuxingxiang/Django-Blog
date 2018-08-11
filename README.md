# Django Blog

基于 Django 开发的博客系统:

- Python 3.7 和 Django 2.1
- MySQL
- xadmin后台管理
- Simditor Markdown 编辑器，图片 Drag and Drop 上传
- 纯 CSS 前端
- RSS订阅
- 标签
- haystack文章内容搜索
- 一级文章评论（TODO：多级评论）

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
python manage.py createsuperuser
```
- 创建搜索索引
```
python manage.py rebuild_index
```
------
### 首页

![index](/github_pic/index.png)

### 详情页

![detail](/github_pic/detail.png)

### 评论

![comments](/github_pic/comments.png)

### Tag List

![tag_list](/github_pic/tag_list.png)

### Tag Detail

![tag_detail](/github_pic/tag_detail.png)

### xadmin后台

![admin](/github_pic/admin.png)

### Simditor Mardown 文章编辑器 图片上传

![pic_upload](/github_pic/pic_upload.png)
