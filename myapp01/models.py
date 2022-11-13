from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Mata:
        # 默認情況下，"QuerySet""返回的結果是根據模型 ''Meta''中的"ordering"選項給出的排序元組排序
        ordering = ('-pub_date',)#回傳必須是字串
        def __str__(self):
            return self.title  

#默認情況下，QuerySet 根據模型 Mata 類的 ordering 選項排序。要使用特定的排序方法時可以用order_by()
# 
# 例如，要 pub_date 字段升序排列，使用以下方法:
# 
# ordering = ['pub_date']
# 要按 pub_date 降序排列，請使用:
# 
# ordering = ['-pub_date']
# 要按 pub_date 降序，然後按 author 升序，請使用:   