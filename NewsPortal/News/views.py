from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from datetime import datetime


class NewsList(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class PostSearch(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



