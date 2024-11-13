from django.contrib import admin
from .models import Author, Blogpost, Category
# Register your models here.

admin.site.register(Author)

admin.site.register(Blogpost)

admin.site.register(Category)
