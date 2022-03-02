from django.db import models

# Create your models here.

class Feed(models.Model):
    content = models.TextField() #글내용
    image = models.TextField()   # 피드 이미지
    profile_image = models.TextField() # 프로필 이미지
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=30, blank=True, null=True) #글쓴이
    like_count = models.IntegerField() #좋아요


