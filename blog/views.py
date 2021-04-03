from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import BlogFormArticle
from django.urls import reverse


class ArticleCreateView(CreateView):        # shablon doredilyar we ony model hemde url bn baglayar..Ozal CreateView durdy
    template_name = 'blog1/article_create_list.html'
    form_class = BlogFormArticle
    queryset = Article.objects.all()
    # success_url= '/'

    def from_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'


class ArticleListView(ListView):        #browserda list doredyar...
    template_name = 'blog1/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'blog1/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):        # shablon doredilyar we ony model hemde url bn baglayar..Ozal CreateView durdy
    template_name = 'blog1/article_create_list.html'
    form_class = BlogFormArticle
    queryset = Article.objects.all()
    # success_url= '/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def from_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog1/article_delete.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('article-list')



