from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(label="사이트 명")
    site_url = forms.CharField(label="사이트 주소")

    class Meta:
        model = Bookmark
        fields = '__all__'
        # 북마크의 모델스.py 에 북마크클래스가 가진 요소 한줄한줄을 필즈라고 함
