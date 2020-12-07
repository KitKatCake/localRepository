from django.contrib import admin

from HelloWorld.models import Book,Books,Publish

# Register your models here.

admin.site.register(Book)
admin.site.register(Books)
admin.site.register(Publish)
