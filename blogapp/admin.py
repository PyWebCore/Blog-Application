from django.contrib import admin

from .models import Category,Blog,Comment,Reply

class bloginline(admin.TabularInline):
    model=Blog
    extra=1

@admin.register(Category)
class categoryadmin(admin.ModelAdmin):
    inlines=[bloginline]


