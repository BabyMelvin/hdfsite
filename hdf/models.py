from django.db import models


# 创建models
# 用户
class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_email = models.CharField(max_length=64)
    user_password = models.CharField(max_length=128)


# 用户浏览记录
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 限制最多100条记录
    history_num = models.IntegerField(max_length=100)
    history_name = models.CharField(max_length=128)
    history_url = models.CharField(max_length=256)

    @property
    def __str__(self):
        return print("第 %d 条,名称为：%s,网址%s") % (self.history_num, self.history_name, self.history_url)

    def history(request, user_id):
        user = get_object_or_404(Question, pk=user_id)
        try:
            user.history_set.get(pk=request.POST['history'])
        except (KeyError, History.DoesNotExist):
            # TODO Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            # TODO
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL。
            # reverse() 调用将返回一个这样的字符串：'/polls/3/results/' 3 是 question.id 的值
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 业主
class Owner(models.Model):
    owner_name = models.CharField(max_length=256)
    owner_phone = models.CharField(max_length=128)
    owner_wechat = models.CharField(max_length=128)


# 房源信息
class House(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    house_location = models.CharField(max_length=128)
    house_sub_location = models.CharField(max_length=128)
    # type 出租，出售
    house_type = models.CharField(max_length=128)
    # status: 在出售，在出租   已出租  已出售
    house_status = models.CharField(max_length=128)
    # 几室
    house_bedroom = models.IntegerField(max_length=128)
    # 几厅
    house_room = models.IntegerField(max_length=128)
