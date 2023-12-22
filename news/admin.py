from django.contrib import admin

# Register your models here.

admin.site.site_admin = "Johnthan"
admin.site.site_header = "Johnthan"
admin.site.index_title = "Johnthan"

from .models import NewsArticle

admin.site.register(NewsArticle)
