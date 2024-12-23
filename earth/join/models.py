import os
from django.db import models
from users.models import User
from django.utils import timezone
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tutorial_completed = models.BooleanField(default=False)
    has_card_completed = models.BooleanField(default=False)

# 카드 작성(이미지 업로드, 키워드 선택, 사진 설명)
class CardPost(models.Model):
    KEYWORD_CHOICES = [
        ('DISPOSABLES', '일회용품'),
        ('RECYCLING', '분리수거'),
        ('TUMBLER', '텀블러'),
        ('STANDBY_POWER', '대기전력'),
        ('OTHER', '기타'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cardposts')
    image = models.ImageField(upload_to='card/', blank=False)
    explanation = models.TextField(max_length=500)
    keyword = models.CharField(max_length=20, choices=KEYWORD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_finalized = models.BooleanField(default=False) # 프레임까지 완전적용되어야 조회가능

    def __str__(self):
        return f"{self.author.username} - {self.keyword}"

# 프레임 동적관리
class Frame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cardpost = models.ForeignKey(CardPost, on_delete=models.CASCADE, null=True)

# 이미지 저장
class Photo(models.Model):
    card_post = models.ForeignKey(CardPost, on_delete=models.CASCADE, related_name='decorated_images', null=True, blank=True)
    decorated_image = models.ImageField(upload_to = 'join/')# 꾸민 이미지 저장 경로 설정
    update_time = models.DateTimeField()
    point = models.IntegerField("적립금", default = 50) # 포인트 50점 적립

    # 현재 날짜로 저장되도록 수정
    def save(self, *args, **kwargs):
        # decorated_image가 있을 경우 파일 이름 변경
        if self.decorated_image:
            # 파일 확장자 추출
            ext = os.path.splitext(self.decorated_image.name)[1]
            # 새로운 파일 이름 생성
            self.decorated_image.name = f"{timezone.now().strftime('%Y%m%d_%H%M%S')}{ext}"

        # update_time이 비어 있으면 현재 시간으로 설정
        if not self.update_time:
            self.update_time = timezone.now()

        super().save(*args, **kwargs)

#이미지 공유시 포인트 적립을 위함
class ImageShare(models.Model):
    card_post = models.ForeignKey('CardPost', on_delete=models.CASCADE, related_name='shares', null = True)  # 카드와 연결
    point = models.IntegerField("적립금", default = 100) # 포인트 100점 적립

# 카드 작성시 뜨는 월별 토글을 위해 카테고리로 설정
class Category(models.Model):
    MONTH_CHOICES = [
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    name = models.CharField(max_length=2, choices=MONTH_CHOICES, unique=True)  # 월별 선택지로 설정

    def __str__(self):
        return dict(self.MONTH_CHOICES).get(self.name, "Unknown")
