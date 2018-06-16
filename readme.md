# make a hdf site
# use:
	django+bootstrap

## 1.创建项目

```python
django-admin startprocject mysite
```
将会创建

```python
mysite/          # 根目录容器目录
    manage.py    # 使用各种方式管理Django项目命令行
    mysite/      # 引用内部需要到python包
        __init__.py   
        settings.py
        urls.py
        wsgi.py   #WSGI兼容Web服务。
```
	
## 2.运行服务器

```python
$python manage.py runserver
$python manage.py runserver 8080
$python manage.py runserver 0:8080所有服务器公开IP
```

## 3.创建应用

```python
$ python manage.py startapp polls  # 创建polls应用
```

# 2.数据库配置

```python 
$ python manage.py migrate
```
这个 migrate 命令检查 INSTALLED_APPS 设置，为其中的每个应用创建需要的数据表，至于具体会创建什么，这取决于你的 mysite/settings.py 设置文件和每个应用的数据库迁移文件

## 激活模型
现在你的 Django 项目会包含 polls 应用。接着运行下面的命令：

```python
$ python manage.py makemigrations polls
```

迁移是 Django 对于模型定义（也就是你的数据库结构）的变化的储存形式 - 没那么玄乎.

迁移命令会执行哪些 SQL 语句.sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：

```python
$ python manage.py sqlmigrate polls 0001
```

```
 python manage.py check
```
这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。


现在，再次运行 migrate 命令，在数据库里创建新定义的模型的数据表：

```python
$ python manage.py migrate
```
这个 migrate 命令选中所有还没有执行过的迁移.

### 总结

改变模型需要这三步：

* 编辑` models.py `文件，改变模型
* 运行 `python manage.py makemigrations `为模型的改变生成迁移文件。
* 运行 `python manage.py migrate` 来应用数据库迁移。

### 数据库操作 初试 API
我们进入交互式 Python 命令行.

```python
$ python manage.py shell
```
不是简单的使用 "Python" 是因为 manage.py 会设置 `DJANGO_SETTINGS_MODULE `环境变量，这个变量会让 Django 根据 mysite/settings.py 文件来设置 Python 包的导入路径。

```python
from polls.models import Choice, Question  # Import the model
Question.objects.all() #<QuerySet []>

# Create a new Question.
 Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
 q.save()

# Now it has an ID.
q.id

# Access model field values via Python attributes.
q.question_text  #"What's new?"
q.pub_date  # datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.

Question.objects.all() #<QuerySet [<Question: Question object (1)>]>

# 需要__str__()来显示
```

在次运行

```python
from polls.models import Choice, Question

# Make sure our __str__() addition worked.
Question.objects.all() #<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API
Question.objects.filter(id=1)  # <QuerySet [<Question: What's up?>]>
 Question.objects.filter(question_text__startswith='What') #<QuerySet [<Question: What's up?>]>

# Request an ID that doesn't exist, this will raise an exception.
Question.objects.get(id=2) # DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1) # <Question: What's up?>

# Make sure our custom method worked.

q = Question.objects.get(pk=1)
q.was_published_recently() # True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.

q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
q.choice_set.all() #<QuerySet []>
# Create three choices.
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
c.question # <Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
q.choice_set.all() # <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
 q.choice_set.count() # 3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
 Choice.objects.filter(question__pub_date__year=current_year) # <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
```
`filter`函数利用了`__`作为方法的引用。