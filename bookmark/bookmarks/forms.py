from django import forms
from .models import Bookmark


# 장고의 "꽃"
# - 빈 폼을 보여주는 역할
# - 폼을 통해 입력된 값을 검증하고 저장하는 역할

class BookmarkForm(forms.ModelForm):
    # title = forms.CharField()
    # url = forms.URLField()
    # memo = forms.CharField()


    # 어떤 모델과 어떤 필드들을 등록을 할거냐?를 알려줘야합니다.
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'memo']