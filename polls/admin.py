from django.contrib import admin
from .models import Question, Choice


# Register your models here.
# 第二种方法 在Question后台也i按边界默认提供3个足够的选项字段
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    # 说到拥有数十个字段的表单，你可能更期望将表单分为几个字段集：
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    # 列表列出展示对象
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# 第一种方法比较低效
# admin.site.register(Choice)
