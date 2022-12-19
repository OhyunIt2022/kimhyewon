from django.shortcuts import redirect, render

from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


# from bookmarks.models import Bookmark
# def bookmark_list(request):
#     bookmark_list = Bookmark.objects.all()
#     context = {'bookmark_list':bookmark_list}
#     return render(request, 'bookmark_list.html', context)


# def bookmark_detail(request, pk):
#     # bookmark = Bookmark.objects.get(id=pk)
#     bookmark = get_object_or_404(Bookmark, id=pk)

#     context = {'bookmark' : bookmark}
#     return render(request, 'bookmark_detail.html', context)


# from .forms import BookmarkForm
# def bookmark_create(request):
#     # if request.method == 'POST':
#     #     context = {'text':'POST METHOD!!!'}
#     #     return render(request, 'templates/bookmark_create.html', context)
#     # context={'text':'GET METHOD!!!'}    
#     # return render(request, 'templates/bookmark_create.html', context)
#     # bookmark = Bookmark()
#     # if request.method == 'POST':
#     #     bookmark.title = request.POST['title']
#     #     bookmark.url = request.POST['url']
#     #     bookmark.memo = request.POST['memo']

#     #     bookmark.save()

#     #     return redirect(f'/bookmark/{bookmark.id}/')
        
#     # return render(request, 'templates/bookmark_create.html')

#     # 사전형으로 html 파일에서 사용할 변수를 입력받기
#     # context = {}
#     # if request.method == 'POST':
#     #     form = BookmarkForm(request.POST or None)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect(form)

#     context = {}
    
#     if request.method == 'POST':
#         form = BookmarkForm(request.POST)
#         if form.is_valid():
#             bookmark = form.save()
#             return redirect('bookmarks:detail', bookmark.id)
            
#     else:
#         form = BookmarkForm()
#         context['form']= form


#     return render(request, 'bookmark_create.html', context)


# from django.shortcuts import get_object_or_404
# def bookmark_update(request, pk):
#     # bookmark = Bookmark.objects.get(id=pk)
#     bookmark = get_object_or_404(Bookmark, id=pk)
#     # context={'bookmark':bookmark}

#     # if request.method == 'POST':
#     #     bookmark.title = request.POST['title']
#     #     bookmark.url = request.POST['url']
#     #     bookmark.memo = request.POST['memo']

#     #     bookmark.save()

#     #     return redirect(f'/bookmark/{bookmark.id}/')
        
#     # return render(request, 'templates/bookmark_update.html', context)


#     context = {}
    
#     if request.method == 'POST':
#         form = BookmarkForm(request.POST, instance=bookmark)
#         if form.is_valid():
#             bookmark = form.save()
#             return redirect('bookmarks:detail', bookmark.id)
            
#     else:
#         form = BookmarkForm(instance=bookmark)
#         context['form']= form


#     return render(request, 'templates/bookmark_update.html', context)





# def bookmark_delete(request, pk):
#     # bookmark = Bookmark.objects.get(id=pk)
#     bookmark = get_object_or_404(Bookmark, id=pk)

#     if request.method == 'POST':
#         bookmark.delete()
#         # return redirect('/bookmark/')
#         return redirect('bookmarks:list')

        
#     return render(request, 'templates/bookmark_delete.html')




from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# class BookmarkListView(ListView):
#     model = Bookmark
#     # 적지 않으면 object_list 라는 변수명으로 접근해야함
#     # context_object_name = 'bookmark_list'
#     template_name = 'bookmark_list.html'


# class BookmarkDetailView(DetailView):
#     model = Bookmark
#     context_object_name = 'bookmark'
#     template_name = 'bookmark_detail.html'


# from django.urls import reverse_lazy
# class BookmarkCreateView(CreateView):
#     model = Bookmark
#     form_class = BookmarkForm
#     success_url = reverse_lazy('bookmarks:list')
#     # template_name = 'bookmark_create.html'

# class BookmarkUpdateView(UpdateView):
#     model = Bookmark
#     form_class = BookmarkForm
#     success_url = reverse_lazy('bookmarks:list')
#     # template_name = 'bookmark_update.html'
#     context_object_name = 'bookmark'


# class BookmarkDeleteView(DeleteView):
#     model = Bookmark


from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Bookmark
from .forms import BookmarkForm
class BookmarkListView(ListView):
    # 1. model정하기
    model = Bookmark
    
    # 2. html파일에서 사용할 변수명 정하기
    context_object_name = 'bookmark_list'

    # 3. 어떤 templates(html)와 연결해줄지 정하기
    # template_name = 'bookmark_list.html'

    # BASE_DIR/templates/bookmark_list.html

    # BASE_DIR/templates/bookmarks/bookmark_list.html



class BookmarkDetailView(DetailView):
    model = Bookmark
    context_object_name = 'bookmark'
    # template_name = 'bookmark_detail.html'


from django.urls import reverse_lazy
class BookmarkCreateView(CreateView):
    model = Bookmark
    form_class = BookmarkForm
    success_url = reverse_lazy('bookmarks:list')
    # template_name = 'bookmark_create.html'


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    context_object_name = 'bookmark'
    form_class = BookmarkForm
    success_url = reverse_lazy('bookmarks:list')
    # template_name = 'bookmark_update.html'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmarks:list')
    # template_name = 'bookmark_delete.html'