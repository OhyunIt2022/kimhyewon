from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class PostListView(ListView):
    # 1. 모델지정해주기
    model = Post
    # 2. 변수명
    context_object_name = 'post_list'
    # 3. templates 지정해주기 => 안해줄거임!(자동으로 지정됨)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blogapp:list')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'post_update'
    form_class = PostForm
    success_url = reverse_lazy('blogapp:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogapp:list')
