from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','body','pub_date')#讓文章在管理者介面顯示除了title之外，還可以有張貼的日期和時間

admin.site.register(Post, PostAdmin)#PostAdmin : 就是要將上面list_display的資料，在資料庫顯示出你想要看到的資料
                                    #Post : models.py的資料表模型，在資料庫顯示出來