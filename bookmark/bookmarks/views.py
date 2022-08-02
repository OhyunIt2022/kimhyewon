from django.shortcuts import render



from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


from bookmarks.models import Bookmark
def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    context = {'bookmark_list':bookmark_list}
    return render(request, 'templates/bookmark_list.html', context)