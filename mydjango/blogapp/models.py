from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='글 제목', max_length=30)
    context = models.TextField(verbose_name='글 내용')

    # 최초 저장시에만 수정되는 필드
    created_at = models.DateTimeField(verbose_name='작성시간', auto_now_add=True)
    # 수정할떄마다 갱신되는 필드
    updated_at = models.DateTimeField(verbose_name='수정시간', auto_now=True)