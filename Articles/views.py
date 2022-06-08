from django.shortcuts import render
from django.views.generic import (ListView, DetailView,CreateView,UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




from .models import Article


# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'ArticleListView.html'
    ordering = ['date']
    paginate_by: 5

class ArticleDetailView(DetailView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Article

    template_name = 'ArticleDetailView.html'
#here we wont specify a template and we will put it in the place where it will be default looked for.

class ArticleCreateView(LoginRequiredMixin, CreateView):
# the reason that the mixin has to be first is that the inheritence is read from left to right
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Article

    fields = ['title', 'body',]

    template_name = 'ArticleCreateView.html' 

    success_url = ""

    def form_valid(self, form):
        form.instance.author = self.request.user
#here we are ovveriding the natural save method which apparently is called form valid and setting 
#the author field as the logged in user which we created in models. You can also add the author field
#but that just ends up displaying all the authors to everyone. 
        return super().form_valid(form)
#to chap these things need the source code for the forms class, but it runningt he form valid method
#on the parent class cuz we reset it here we need to run it ourselves??

#the fields here are just the fields in the post objects 

#cant use decorators on classes so need some other way to make sure the post creator is logged in 
#so they have a thing 

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#the mixins need to be to the left of the updateview
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Article

    fields = ['title', 'body',]

    def form_valid(self, form):
        form.instance.author = self.request.user
#here we are ovveriding the natural save method which apparently is called form valid and setting 
#the author field as the logged in user which we created in models. You can also add the author field
#but that just ends up displaying all the authors to everyone. 
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#remember that im creating the new class here even when using built in django stuff im just allowed 
#to inherit from listview here so i will already have methods
    model = Article

    success_url = 'articles/'

    def test_func(self):
        body = self.get_object()
        if self.request.user == body.author:
            return True
        return False


