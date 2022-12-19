from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('create', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/',views.PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(), name='delete')
]