from django.contrib import admin
from .models import ArticleModel,Article,Comment
# Register your models here.
admin.site.register(ArticleModel)
admin.site.register(Article)
admin.site.register(Comment)




