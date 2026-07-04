from django.db import models
from django.conf import settings

class Video(models.Model):
    channel = models.ForeignKey('channels.Channel', on_delete=models.CASCADE, related_name='videos')
    video_url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_edited = models.BooleanField(default=False)

    class Meta:
        db_table = 'comments'

class View(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='views')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views')
    created_at = models.BooleanField(default=True)

    class Meta:
        db_table = 'view'

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        db_table = 'likes'
        unique_together = ('user', 'video')

class Dislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='dislikes')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='dislikes')

    class Meta:
        db_table = 'dislikes'
        unique_together = ('user', 'video') 