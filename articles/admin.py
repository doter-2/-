from django.contrib import admin

# Register your models here.
from .models import Articles, News
admin.site.register(Articles)
admin.site.register(News)