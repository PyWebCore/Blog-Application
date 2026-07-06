from django.shortcuts import render,redirect
from .models import Blog
from django.views.generic import CreateView,ListView


class bloglist(ListView):
    model=Blog
    template_name="blogapp/list.html"
    context_object_name="blogs"
    paginate_by=5

