from django.urls import path
from bookmarkapp import views


# 1. mysite/urls.py에서 복붙한다.
# 2. detail 페이지로 가서 url의 문제점을 얘기한다.
# 3. urls.py 돌아와서 name을 적어준다.

app_name = 'bookmarkapp'



urlpatterns = [
    # path('', views.bookmark_list,name='list'),
    # path('<int:pk>/', views.bookmark_detail, name='detail'),
    # path('create/', views.bookmark_create, name='create'),
    # path('update/<int:pk>/',views.bookmark_update, name='update'),
    # # path('<int:pk>/update/',views.bookmark_update, name='update'),

    # # localhost:8000/bookmark/10/update/
    # # localhost:8000/bookmark/update/10/
    # path('delete/<int:pk>/',views.bookmark_delete, name='delete'),

    path('new/', views.BookmarkListView.as_view(), name='list'),
    path('new/<int:pk>/', views.BookmarkDetailView.as_view(), name='detail'),
    path('new/create/', views.BookmarkCreateView.as_view(), name='create'),
    path('new/update/<int:pk>/', views.BookmarkUpdateView.as_view(), name='update'),
    path('new/delete/<int:pk>/', views.BookmarkDeleteView.as_view(), name='delete'),
    


]

# localhost:8000/bookmark/bookmark/

# 학교로 비교
# 2-1 ㅇㅇㅇ 2-2 ㅇㅇㅇ
# app_name = 'comment'
# localhost:8000/accounts/profile/update/1/ -> name='update'