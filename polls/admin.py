from django.contrib import admin
# Register your models here.
from .models import Post
from .models import About
from .models import Member

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Member)
