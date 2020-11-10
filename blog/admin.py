from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog

class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    
    list_per_page = 25
    summernote_fields = ('content', )

from django.contrib import admin

from .models import Blog

admin.site.register(Blog, BlogPostAdmin)
