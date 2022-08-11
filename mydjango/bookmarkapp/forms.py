from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    # title = forms.CharField()
    # url = forms.URLField()
    # memo = forms.CharField()
    class Meta:
        model = Bookmark
        fields = ['title','url','memo']
        # fields = '__all__'