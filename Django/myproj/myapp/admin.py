from django.contrib import admin
# from myapp.models import Task
from booking.models import Author, Book, Tag
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)